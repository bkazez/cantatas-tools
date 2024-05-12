import urllib.parse
import webbrowser
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
import sys
import json

def get_url_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def parse_xml(content):
    root = ET.fromstring(content)
    ns = {'mods': 'http://www.loc.gov/mods/v3'}
    return root, ns

def extract_data_from_xml(url, content):
    root, ns = parse_xml(content)

    data = {
        'title': '', 'author': '', 'year_of_publication': '',
        'isbn': '', 'oclc': '', 'lccn': '', 'publisher': '',
        'physical_description': '', 'series_title': '', 'series_part_number': '',
        'fromWhat': '',
    }

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
        series_title = series_element.find('.//mods:title', ns)
        series_part_number = series_element.find('.//mods:partNumber', ns)
        data['series_title'] = series_title.text if series_title else ""
        data['series_part_number'] = series_part_number.text if series_part_number else ""

    # Extract author information
    first_personal_name = root.find('.//mods:name[@type="personal"]', ns)
    if first_personal_name:
        primary_name_part = first_personal_name.find('mods:namePart', ns)
        author_date = first_personal_name.find('mods:namePart[@type="date"]', ns)
        data['author'] = (primary_name_part.text.strip(',') if primary_name_part else "") + (f" ({author_date.text})" if author_date else "")

    # Extract publishing information
    origin_info = root.find('.//mods:originInfo', ns)
    if origin_info:
        publisher_name_part = origin_info.find('mods:agent/mods:namePart', ns)
        date_issued = origin_info.find('mods:dateIssued', ns)
        data['publisher'] = publisher_name_part.text if publisher_name_part else ""
        data['year_of_publication'] = date_issued.text if date_issued else ""

    # Extract physical description
    physical_description = root.find('.//mods:physicalDescription/mods:extent', ns)
    data['physical_description'] = physical_description.text if physical_description else ""

    # Extract identifiers
    for id_type in ['isbn', 'oclc', 'lccn']:
        identifier = root.find(f'.//mods:identifier[@type="{id_type}"]', ns)
        if identifier:
            data[id_type] = identifier.text.strip('ocn') if id_type == 'oclc' and identifier.text else identifier.text if identifier else ""

    return data

def extract_from_html(url, content):
    soup = BeautifulSoup(content, 'html.parser')
    json_ld_script = soup.find('script', type='application/ld+json')
    if json_ld_script:
        try:
            data = json.loads(json_ld_script.string)
            return {
                'title': data.get("name", ""),
                'author': data.get("author", {}).get("name", ""),
                'publisher': data.get("publisher", ""),
                'fromWhat': url
            }
        except json.JSONDecodeError:
            return None

    return None

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
        'isbn': data['isbn'],
        'oclc': data['oclc'],
        'lccn': data['lccn'],
        'edition': '. '.join(filter(None, [data['publisher'], data['series_title'], data['series_part_number'], data['physical_description']])),
        'fromWhat': data['fromWhat']
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
