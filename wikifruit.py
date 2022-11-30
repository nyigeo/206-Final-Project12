import json
import unittest
import os
import requests
import re 
from xml.sax import parseString
from bs4 import BeautifulSoup


url = 'https://simple.wikipedia.org/wiki/List_of_fruits'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
#var = 'component page-object text'
pay = soup.find_all('ul', class_= "mw-body-content mw-content-ltr")
#listofpay = []
#print(soup)
# for tag in pay:
#     print(tag.text)
# something = tag.find_all('p')
# if len(something) != 0:
#listofpay.append(something[0].text)
for data in pay: 
   print(data)