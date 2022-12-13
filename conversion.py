import json
import unittest
import os
import requests
import re 
import sqlite3
from xml.sax import parseString
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import tropical 


def get_temperature(avo):
    avocado_results = tropical.get_request_url(avo)
    avocado_dict = json.loads(avocado_results) 
    climate_info =str(avocado_dict['results'][0]['climate'])
    if 'temperature' in climate_info:
        if re.search(r'(-*\d+)',climate_info) != None:
            fruit_temp = re.findall(r'(-*\d+)',climate_info)
            list_temp = []
            fruits = tropical.get_tropical_list_wiki()
            for fruit in fruits:
                list_temp.append((fruit, get_temperature(fruit)))
            for t in list_temp:
                string = list_temp[t[1]]
                match = fruit_temp.search(string)
            if match:
                matched_string = match.group()
                value = int(matched_string)
                fahrenheit = (value * 1.8) + 32
                updated_string = fruit_temp.sub(str(fahrenheit),string)
            return updated_string
        print(list_temp)
        return fruit_temp[0]
    else: 
        return None

def main():
   pass
  
if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)