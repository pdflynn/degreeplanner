#!/usr/bin/env python3
# Web scraper (simple) for pulling data from VT's Banner timetable information.

import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

# Returns the URL for a specified course
def get_course_url(crn, year, subj, crse):
    url = "https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcComments?" + "CRN=" + crn + "&YEAR=" + year + "&SUBJ=" + subj + "&CRSE=" + crse
    return url

# Returns a list of prerequisite courses for the specified course URL
def get_prerequisites(url):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get(url)
    prereqs = [] # store prerequisite courses as strings
    # webbrowser.open(url, new=2)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    content = soup.findAll('td', class_='pldefault')
    for a in content:
        tag = str(a)
        match = re.findall(r'(>[^<]*</a)', tag)
        for course in match:
            prereqs.append(course[1:-3])
    print(prereqs)
    return prereqs

get_prerequisites(get_course_url("88740", "2020", "NR", "4014"))