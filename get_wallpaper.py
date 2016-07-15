#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import random

url = 'https://unsplash.com/'
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')
data = soup.findAll(
    'a',
    attrs={
        'class': 'cV68d'
    }
)
img = random.choice(data)
link = '{}{}/download'.format(url[:-1], img.get('href'))
print(link)
