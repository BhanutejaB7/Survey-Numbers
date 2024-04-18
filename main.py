import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    # Base URL of the website
    base_url = "https://dharani.telangana.gov.in/knowLandStatus"

    # Make a POST request to the website with district, mandal, and village data
    data = {
        'districtCode': district,
        'mandalCode': mandal,
        'villageCode': village,
        'mandalname': '',
        'villagename': '',
        'surveyNo': ''
    }
    response = requests.post(base_url, data=data)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the survey numbers and store them in a list
    survey_numbers = []
    survey_select = soup.find('select', {'id': 'surveyNo'})
    if survey_select:
        for option in survey_select.find_all('option'):
            survey_numbers.append(option.text.strip())

    return survey_numbers


# Example usage
district = '01'  # District code (e.g., '01' for Adilabad)
mandal = '01'    # Mandal code
village = '01'   # Village code
survey_numbers = get_survey_numbers(district, mandal, village)
print("Survey Numbers:")
for survey_number in survey_numbers:
    print(survey_number)
