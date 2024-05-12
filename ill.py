import urllib.parse
import webbrowser
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
import sys
import re
import html
import json

def get_url_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def parse_xml(content):
    root = ET.fromstring(content)
    ns = {'mods': 'http://www.loc.gov/mods/v3'}
    return root, ns

def empty_data():
    return {
        'title': '', 'author': '', 'year_of_publication': '',
        'oclc': '', 'lccn': '', 'publisher': '',
        'physical_description': '', 'series_title': '', 'series_part_number': '',
        'fromWhat': '',
    }

def extract_data_from_xml(url, content):
    root, ns = parse_xml(content)

    data = empty_data()

    if url:
        data['fromWhat'] = url[:-5] if url.endswith('/mods') else url

    # Extract title and subtitle
    title_element = root.find('.//mods:titleInfo', ns)
    if title_element:
        title = title_element.find('mods:title', ns)
        subTitle = title_element.find('mods:subTitle', ns)
        data['title'] = (title.text if title is not None else "") + (f": {subTitle.text}" if subTitle else "")

    # Extract series information

    series_element = root.find('.//mods:relatedItem[@type="series"]', ns)
    if series_element:
        series_title = series_element.find('.//mods:titleInfo/mods:title', ns)
        series_part_number = series_element.find('.//mods:titleInfo/mods:partNumber', ns)
        data['series_title'] = series_title.text if series_title is not None else ""
        data['series_part_number'] = series_part_number.text if series_part_number is not None else ""

    # Extract author information
    first_personal_name = root.find('.//mods:name[@type="personal"]', ns)
    primary_name_part = first_personal_name.find('mods:namePart', ns).text.strip(',')
    author_date = first_personal_name.find('mods:namePart[@type="date"]', ns)
    author_date = f" ({author_date.text})" if author_date is not None else ''
    data['author'] = primary_name_part + author_date

    # Extract publishing information
    publication_info = root.find('.//mods:originInfo[@eventType="publication"]', ns)
    if publication_info:
        publisher_element = root.find('.//mods:originInfo[@eventType="publication"]/mods:agent/mods:namePart', ns)
        data['publisher'] = publisher_element.text.strip(',') if publisher_element is not None else ''

        date_issued = publication_info.find('mods:dateIssued', ns)
        data['year_of_publication'] = date_issued.text if date_issued is not None else ''

    # Extract physical description
    physical_description = root.find('.//mods:physicalDescription/mods:extent', ns)
    data['physical_description'] = physical_description.text if physical_description is not None else ""

    # Extract identifiers
    for id_type in ['oclc', 'lccn']:
        identifier_elements = root.findall(f'.//mods:identifier[@type="{id_type}"]', ns)
        for identifier in identifier_elements:
            identifier_text = identifier.text if identifier is not None else ''
            # Remove any leading non-numeric characters for 'oclc' identifiers
            if id_type == 'oclc':
                # Using regex to find the first sequence of digits and ignore non-digit prefixes
                match = re.search(r'\d+', identifier_text)
                identifier_text = match.group(0) if match else ''
            data[id_type] = identifier_text
            # Assuming only one identifier per type is needed, break after finding the first valid one
            if identifier_text:
                break

    return data

def extract_from_html(url, content):
    soup = BeautifulSoup(content, 'html.parser')
    json_data_script = soup.find('script', {'type': 'application/json'}, id='__NEXT_DATA__')
    if json_data_script:
        try:
            data_json = json.loads(json_data_script.string)
            record = data_json['props']['pageProps']['record']
            data = empty_data()
            data.update({
                'title': record.get("title", ""),
                'author': record.get("creator", ""),
                'publisher': record.get("publisher", ""),
                'year_of_publication': record.get("publicationDate", ""),
                'physical_description': record.get("physicalDescription", ""),
                'series_title': record.get("series", ""),
                'series_part_number': ','.join(record.get("seriesVolumes", "")),
                'oclc': record.get("oclcNumber", ""),
                'fromWhat': url,
            })
            print(data)
            return data
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return None
        except KeyError as e:
            print(f"Key error: {e}")
            return None
    else:
        print("Unable to find the required JSON data.")
        sys.exit(1)

def generate_prefilled_jotform_url(data):
    if not data:
        print("Error: No data to generate URL.")
        return None

    # Base URL of the JotForm
    base_url = "https://wittenberg.jotform.com/202176782372155"

    # Dictionary of form parameters and values
    form_data = {
        'parentURL': 'https://www.wittenberg.edu/lib/services/forms/ill_book',
        'jsForm': 'true',
        'name[first]': 'Daniel',
        'name[last]': 'Kazez',
        'wittenbergAffiliation': 'Faculty',
        'email': 'dkazez@wittenberg.edu',
        'phoneNumber[area]': '937',
        'phoneNumber[phone]': '327-7354',
        'department': 'Music',
        'iHave13': 'Yes',
        'iAm41': 'my own project/assignment',
        'ifThis': 'No',
        'title': data['title'],
        'author': data['author'],
        'yearOf': data['year_of_publication'],
        'oclc': data['oclc'],
        'lccn': data['lccn'],
        'edition': '. '.join(filter(None, [data['publisher'], data['series_title'], data['series_part_number'], data['physical_description']])),
        'fromWhat': data['fromWhat'],
    }

    # Encode the parameters
    encoded_params = urllib.parse.urlencode(form_data, quote_via=urllib.parse.quote)

    # Construct the full URL
    full_url = f"{base_url}?{encoded_params}"
    return full_url

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    content = get_url_content(url)
    if "worldcat.org" in url:
        extracted_data = extract_from_html(url, content)
    else:
        extracted_data = extract_data_from_xml(url, content)

    if not extracted_data:
        print("Failed to extract data.")
        sys.exit(1)

    jotform_url = generate_prefilled_jotform_url(extracted_data)
    if jotform_url:
        webbrowser.open(jotform_url)

if __name__ == "__main__":
    main()
