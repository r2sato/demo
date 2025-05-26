import requests
from bs4 import BeautifulSoup

# Get
res = requests.get('https://www.google.com/')

# Parse
soup = BeautifulSoup(res.text, 'html.parser')

# title
title = soup.find('title').text

print(title)


