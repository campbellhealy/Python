# Indeed Job Search

import json
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Search URL
URL = "https://www.indeed.co.uk/jobs?q=test+analyst+%2420%2C000&l=Scotland&start=10"

# GET request converted into a data_object:
data_object = requests.get(URL)

# Format of data_object using the html parser.
soup = BeautifulSoup(data_object.text, "html.parser")

# Use this on first run to get the raw object
# print(soup.prettify())

# ----- This section lists out the job titles related to what was put in the URL Search ------
jobs = []


def extract_job_title(soup):
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element": "jobTitle"}):
            jobs.append(a["title"])
    return jobs


extract_job_title(soup)
jj = jobs
# ----- This section lists out the job titles related to what was put in the URL Search ------

# ----- This section lists out the Companyies related to  the URL Search ------
companies = []


def extract_company(soup):
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        company = div.find_all(name="span", attrs={"class": "company"})
        if len(company) > 0:
            for b in company:
                companies.append(b.text.strip())
            else:
                sec_try = div.find_all(
                    name="span", attrs={"class": "result-link-source"}
                )
            for span in sec_try:
                companies.append(span.text.strip())
    return companies


extract_company(soup)
cc = companies
# ----- This section lists out the Companyies related to  the URL Search ------

# ----- This section lists out the Salary related to  the URL Search ------
salaries = []


def extract_salary(soup):
    spans = soup.findAll("span", attrs={"class": "salaryText"})
    for span in spans:
        salaries.append(span.text)
    return salaries


extract_salary(soup)
ss = salaries
# ----- This section lists out the Salary related to  the URL Search ------

# ----- This section lists out the Locations related to  the URL Search ------
locations = []


# def extract_location(soup):
#     spans = soup.findAll("span", attrs={"class": "location"})
#     for span in spans:
#         locations.append(span.text)
#     return locations


# extract_location(soup)
# ll = locations
# ----- This section lists out the Locations related to  the URL Search ------


# ----- This section lists out the Description related to  the URL Search ------
descriptions = []


# def extract_descriptions(soup):
#     spans = soup.findAll("span", attrs={"class": "summary"})
#     for span in spans:
#         descriptions.append(span.text.strip())
#     return descriptions


# extract_descriptions(soup)
# dd = descriptions

# ----- This section lists out the Description related to  the URL Search ------

# ----- This section lists out the link related to  the URL Search ------
links = []


def extract_link(soup):
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        for a in div.find_all(name="a"):
            if a == None:
                a = "#"
            else:
                links.append(a.get("href"))

        return links


extract_link(soup)
lin = links
# ----- This section lists out the link related to  the URL Search ------

vacancies = [
    (job, company, salary, link)  # , description)
    for job in jj
    for company in cc
    for salary in ss
    for link in lin
    # for location in ll
    # for description in dd
]
the_list = []
for post in vacancies:
    print(post)
    the_list += post

with open(
    "list.json", "w"
) as f:  # Writes a new file, 'jobs.json' with the altered set from elements in the python object above
    json.dump(
        the_list, f, indent=2
    )  # indent attribute helps format the data to look like JSON
