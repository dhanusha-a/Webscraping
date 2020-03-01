#!/usr/bin/env python
import requests
page=requests.get("https://www.webscraper.io/test-sites/e-commerce/allinone/computers")
print (page)
print (page.status_code)
print ("---------------------------------------------------------------------------")

print (page.content)
print ("---------------------------------------------------------------------------")

#------------------------------------------------------------------------------------

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
print ("---------------------------------------------------------------------------")
print (soup.prettify())
print ("---------------------------------------------------------------------------")
print (list (soup.children))
print ("---------------------------------------------------------------------------")
name = soup.find('a',class_="title").text
print (name)
price = soup.find('h4',class_="pull-right price").text
print (price)

#-----------------------------------------------------------------------------------

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, price, datetime.now()])
