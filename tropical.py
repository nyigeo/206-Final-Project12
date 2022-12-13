import json
import unittest
import os
import requests
import re 
import sqlite3
from xml.sax import parseString
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def get_request_url(tropicalfruit):
    r = requests.get(f'http://api.tropicalfruitandveg.com/tfvjsonapi.php?tfvitem={tropicalfruit}')
    return r.text

def get_request_url2(all):
    r = requests.get(f'https://tropicalfruitandveg.com/api/tfvjsonapi.php?search={all}')
    print(r.text)
    # return r.text

def get_tropical_list_wiki():
    url = 'https://www.tropicalfruitandveg.com/tfvlista-z.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    pay = soup.find_all('a')
    fruits=[]
    for li in pay:
        fruits.append(li.text)
    cleaned_fruits=[]
    for i in fruits[22:-18]:
        if i != '':
            cleaned_fruits.append(i)
    return cleaned_fruits


def get_temperature(avo):
   avocado_results = get_request_url(avo)
   avocado_dict = json.loads(avocado_results)
   climate_info = avocado_dict['results'][0]['climate']
   if 'temperature' in climate_info:
       if re.search(r'(-*\d+.\s*[CF])',climate_info) != None:
           fruit_temp = re.findall(r'(-*\d+.\s*[CF])',climate_info)
           return fruit_temp[0]
   else:
            return None

def main():
    fruits = get_tropical_list_wiki()
    list_temp = []
    for fruit in fruits:
        list_temp.append((fruit, get_temperature(fruit)))
    print(list_temp)
  
if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)

