import urllib.parse
import webbrowser
import xml.etree.ElementTree as ET
import requests
import sys

def download_and_parse_xml(url):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    # Parse the XML response content
    root = ET.fromstring(response.content)

    # Define the namespace
    ns = {'mods': 'http://www.loc.gov/mods/v3'}

    # Extract elements for the title and subtitle
    title_element = root.find('.//mods:titleInfo', ns)
    title = title_element.find('mods:title', ns).text
    subTitle = title_element.find('mods:subTitle', ns)
    subTitle = f" : {subTitle.text}" if subTitle is not None else ""
    full_title = title + subTitle

    # Handling relatedItem type "series"
    series_element = root.find('.//mods:relatedItem[@type="series"]', ns)
    if series_element is not None:
        series_title = series_element.find('.//mods:title', ns).text
        series_part_number = series_element.find('.//mods:partNumber', ns).text
    else:
        series_title = ''
        series_part_number = ''

    # Extract author's primary name part and date
    first_personal_name = root.find('.//mods:name[@type="personal"]', ns)
    primary_name_part = first_personal_name.find('mods:namePart', ns).text.strip(',')  # Finds the first namePart
    author_date = first_personal_name.find('mods:namePart[@type="date"]', ns)
    author_date = f" ({author_date.text})" if author_date is not None else ''
    author = primary_name_part + author_date

    # Origin Info for agent and dateIssued
    publisher = root.find('.//mods:originInfo/mods:agent/mods:namePart', ns).text
    date_issued = root.find('.//mods:originInfo/mods:dateIssued', ns).text

    # Extract physical description as edition
    physical_description = root.find('.//mods:physicalDescription/mods:extent', ns)
    physical_description = physical_description.text if physical_description is not None else ''

    # Extract ISBN, OCLC, LCCN
    isbn = root.find('.//mods:identifier[@type="isbn"]', ns)
    oclc = root.find('.//mods:identifier[@type="oclc"]', ns)
    lccn = root.find('.//mods:identifier[@type="lccn"]', ns)

    isbn = isbn.text if isbn is not None else ''
    oclc = oclc.text.replace('ocn', '') if oclc is not None else ''
    lccn = lccn.text if lccn is not None else ''

    return {
        'title': full_title,
        'author': author,
        'year_of_publication': date_issued,
        'isbn': isbn,
        'oclc': oclc,
        'lccn': lccn,
        'publisher': publisher,
        'physical_description': physical_description,
        'series_title': series_title,
        'series_part_number': series_part_number,
        'fromWhat': url[:-5] if url and url.endswith('/mods') else 'https://www.wittenberg.edu/lib/services/forms/ill_book'
    }

def generate_prefilled_jotform_url(data):
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

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else None
    extracted_data = download_and_parse_xml(url) if url else None

    # Generate the URL
    url_to_open = generate_prefilled_jotform_url(extracted_data)

    # Open the URL in the default browser
    webbrowser.open(url_to_open)
