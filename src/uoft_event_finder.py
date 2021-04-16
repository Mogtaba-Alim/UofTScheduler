"""Uses the Beautiful Soup webscraper to scrape throughout the 'https://www.utoronto.ca/events'
    website and returns the links of the upcoming events being held
"""

import requests
from bs4 import BeautifulSoup
import pprint

def find_events() -> None:
    """Uses webscraping to find upcoming events at U of T"""
    url = 'https://www.utoronto.ca/events'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    urls = urls[43:106]
    pprint.pprint(urls)
