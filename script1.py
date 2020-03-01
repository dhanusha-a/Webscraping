#!/usr/bin/env python
import requests
page=requests.get("https://www.webscraper.io/test-sites/e-commerce/allinone/phones/touch")
print (page)
print (page.status_code)
print ("-----------------------------------------------------Content------------------------------------------------------------------------")

#print (page.content)
print ("-----------------------------------------------------------------------------------------------------------------------------")

#---------------------------------------------------------------------------------------------------------------------------------------

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
print ("\n----------------------------------------------Structure using soup-----------------------------------------------------------------")
#print (soup.prettify())

print ("\n--------------------------------------------------------Name-----------------------------------------------------------------------")
name = soup.findAll('a',class_="title")
#print (name)
print ("\n-------------------------------------------------------Price-----------------------------------------------------------------------")
price = soup.findAll('h4',class_="pull-right price")
#print (price)

print ("\n-----------------------------------------------------------Data--------------------------------------------------------------------")

import itertools
data={}
for (x,y) in zip(name,price):
 a = x.text
 b = y.text
 data[a] = b

print (data)

print("Data extracted")

#-------------------------------------------------------------------------------------------------------------------------------------------

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 for key in data:
  writer.writerow([key, data[key], datetime.now()])

print ("Data inserted in file")


