#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import urllib.request
from bs4 import BeautifulSoup


BASE_URL = 'http://www.bunkerspot.com/'


def get_html(url):
    response = urllib.request.urlopen(BASE_URL)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('div', class_='custom prices-mod orange-header')
    rows = table.find_all("tr")

    #print(table)
    #print(rows)

    projects = []
    for row in rows:

        cols = row.find_all('td')
        print(cols)

        if len(cols) > 0:
            projects.append({
                'location': cols[0].p.text,
                '380': cols[1].p.text,
                '180': cols[2].p.text,
                'mgo': cols[3].p.text
            })

    return projects

 
def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(('location', '380', '180', 'MGO'))

        writer.writerows(
            (project['location'], ', '.join(project['380']), project['180'], project['mgo']) for project in projects
        )


def main():
    projects = []
    projects.extend(parse(get_html(BASE_URL)))

    print('Save...')
    save(projects, 'projects.csv')


if __name__ == '__main__':
    main()