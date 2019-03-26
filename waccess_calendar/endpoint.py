# to be used as a REST api endpoint eventually maybe

import requests
import sys
from bs4 import BeautifulSoup
from string import ascii_lowercase
from urllib.parse import unquote
import re

# parameters we care about


def get_semester_dropdown():
    soup = BeautifulSoup(requests.get("https://ro.umich.edu/calendars").text, 'lxml')
    options = soup.find('select', attrs={'id':'edit-field-term-target-id'}).find_all('option')
    semester_dict = {str(opt.text): opt.get("value") for opt in options}
    return semester_dict

def get_semester_dates(semester, semester_dict):
    if semester not in semester_dict.keys():
        return None
    url = "https://ro.umich.edu/calendars?field_calendar_type_target_id%5B1%5D=1&field_term_target_id=" + semester_dict[semester]

    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    event_names = [re.sub(r'\s$','',re.search(r'text(.*)dates',unquote(a.get("href")))[0][5:-6])
                for a in soup.find_all('a',attrs={'class':'google-add'})]

    # dates for a given event, in the format start_YYYYMMDD/end_YYYYMMDD
    event_dates = [re.sub(r'\s$','',re.search(r'dates(.*)details',unquote(a.get("href")))[0][6:-8])
                for a in soup.find_all('a',attrs={'class':'google-add'})]


    semester_dates = dict(zip(event_names, event_dates))

    return semester_dates


if __name__ == "__main__":
    semester_dict = get_semester_dropdown()

    # # Read sites from input into list
    # json = scrape_page() = ['https://www.rottentomatoes.com/critics/authors?letter=' + c
    #               for c in ascii_lowercase]

    dates_json = get_semester_dates("Winter 2019", semester_dict)
    # Generate and print list of author usernames
    print(dates_json)