from bs4 import BeautifulSoup
import requests
import os
import urllib.request

source = requests.get('http://explosm.net/comics/archive').text
soup = BeautifulSoup(source, 'lxml')

#input syntx
with open('range.txt') as f:
    lines=[i.rstrip('\n')for i in f]
(start_month,start_year)=lines[0].split()
(end_month,end_year)=lines[1].split()
author=lines[2].split()
start_year=int(start_year)
end_year=int(end_year)
monthlist=['january','february', 'march','april','may','june','july','august','september','october','november','december']
start_month_index=monthlist.index(start_month)
end_month_index=monthlist.index(end_month)
monthdiff=end_month_index-start_month_index+(end_year-start_year)*12

for year in range (start_year,end_year+1):
    if year==start_year:
        imindex=start_month_index
        fmindex=11
    elif year==end_year:
        imindex=0
        fmindex=end_month_index
    else:
        imindex=0
        fmindex=11
    os.makedirs(str(year))
        
    for month in range (imindex,fmindex+1):
        os.makedirs(str(year)+'/'+str(monthlist[month]))
        for name in author:
            if month>8:
                spath= 'http://explosm.net/comics/archive/'+str(year)+'/'+str(month+1)+'/'+str(name)
            else:
                spath='http://explosm.net/comics/archive/'+str(year)+'/0'+str(month+1)+'/'+str(name)
            sourcelist = requests.get(spath).text
            print(spath)
            souplist = BeautifulSoup(sourcelist, 'lxml')
            for downitem in souplist.find_all('div',{'class':'archive-list-item'}):
                id=downitem.a['href']
                print(id)
                sourcefinal = requests.get('http://explosm.net'+str(id)).text
                soupfinal=BeautifulSoup(sourcefinal, 'lxml')
                image=soupfinal.find('img',{'id':'main-comic'})['src']
                image='https://'+image[2:-9]
                imagefile=open(str(year)+'/'+str(monthlist[month])+'/'+str(id[8:-1])+'.jpeg','wb')
                imagefile.write(urllib.request.urlopen(image).read())
                imagefile.close()
'''
#output
# for i in outputfile:
#     path= 'C:/Users/Admin/Desktop/scrapping/output'+str(start_year)+'/'+start_month
#     os.makedirs(path)
imagefile=open('name'+'.jpeg','wb')
#imagefile.write(urllib.request.urlopen('http://files.explosm.net/comics/Kris/fightcloud.png?t=C1CB9B').read())
imagefile.close()
'''