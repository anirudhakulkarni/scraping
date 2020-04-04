from bs4 import BeautifulSoup
import requests
import os

source = requests.get('http://explosm.net/comics/archive').text
soup = BeautifulSoup(source, 'lxml')

#input syntx
with open('range.txt') as f:
    lines=[i.rstrip('\n')for i in f]
(start_month,start_year)=lines[0].split()
(end_month,end_year)=lines[1].split()
author=lines[2]

