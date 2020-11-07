import bs4 as bs
import urllib.request
import pandas as pd
sauce=urllib.request.urlopen('https://accessibility.umn.edu/web-designers/tables-web-pages').read()
soup=bs.BeautifulSoup(sauce,'lxml')
table=soup.table
#print(table)

tab_row=table.find_all('tr')
for tr in tab_row:
    td=tr.find_all('td')
    row=[i.text for i in td]
   
    listToStr = ' '.join([str(elem) for elem in row]) 
    print(listToStr) 
