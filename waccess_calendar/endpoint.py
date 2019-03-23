# to be used as a REST api endpoint eventually maybe

import requests
import sys
from bs4 import BeautifulSoup
from string import ascii_lowercase

# parameters we care about


def get_semester_dropdown():
    soup = BeautifulSoup(requests.get("https://ro.umich.edu/calendars").text, 'lxml')
    options = soup.find('select', attrs={'id':'edit-field-term-target-id'}).find_all('option')
    # url_param = [str(opt.get("value")) for opt in options]
    # sem = [str(opt.text) for opt in options]
    # semester_dict = dict(zip(sem, url_param))
    semester_dict = {str(opt.text): opt.get("value") for opt in options}

    print(semester_dict)
    return semester_dict



def get_semester_dates(semester, semester_dict):
    if semester not in semester_dict.keys():
        return None
    url = "https://ro.umich.edu/calendars?field_calendar_type_target_id%5B1%5D=1&field_term_target_id=" + semester_dict[semester]

    return usernames


if __name__ == "__main__":
    semester_dict = get_semester_dropdown()

    # # Read sites from input into list
    # json = scrape_page() = ['https://www.rottentomatoes.com/critics/authors?letter=' + c
    #               for c in ascii_lowercase]

    # Generate and print list of author usernames
    print(json)