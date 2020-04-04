from bs4 import BeautifulSoup
import requests
import os
import urllib.request

source = requests.get('http://explosm.net/comics/archive').text
soup = BeautifulSoup(source, 'lxml')

starting= soup.find('')
#input syntx
with open('range.txt') as f:
    lines=[i.rstrip('\n')for i in f]
(start_month,start_year)=lines[0].split()
(end_month,end_year)=lines[1].split()
author=lines[2]

#output
# for i in outputfile:
#     path= 'C:/Users/Admin/Desktop/scrapping/output'+str(start_year)+'/'+start_month
#     os.makedirs(path)
imagefile=open('name'+'.jpeg','wb')
imagefile.write(urllib.request.urlopen('http://files.explosm.net/comics/Kris/fightcloud.png?t=C1CB9B').read())
imagefile.close()