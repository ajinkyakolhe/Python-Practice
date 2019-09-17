# Scraping
# Simple application for scraping NGA Museum website page

import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('z-artist_names.csv', 'w'))
f.writerow(['Name', 'Link'])
pages = []
for i in range(1,5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for it in pages:
    page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_ = 'AlphaNav')
    last_links.decompose()



    artist_names = soup.find(class_ = 'BodyText')
    items = artist_names.find_all('a')


    for artist_name in items:
        #print(artist_name.prettify())
        names = artist_name.contents[0]
        #print(names)
        links = "https://web.archive.org" + artist_name.get('href')
        print(links)
        f.writerow([names, links])
