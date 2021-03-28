import re
from pprint import pprint
import csv
import requests
from bs4 import BeautifulSoup


url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
                     
for row in table.findAll('tr')[0:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
  
for line in list_of_rows:
    row = '\t'.join(str(i) for i in line)  # python 2
    s=row[0:5] # Select only the Last names (1st column)
    m = re.search(r"^A",s,re.I)
    if m:
      print (row)