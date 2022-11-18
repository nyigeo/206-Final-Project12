import json
import unittest
import os
import requests
import re 
from xml.sax import parseString
from bs4 import BeautifulSoup

API_KEY = "5b17fb869d9cf530dd9a6b45cf9228bf"
HEADERS = {'Authorization': 'Bearer {}'.format(API_KEY),
           'User-Agent': 'YelpEventAnalyzer',
           'From': 'himharis@icloud.com',
           'Course-Info': 'https://si.umich.edu/programs/courses/507'
}

def read_json(cache_filename):
    try: 
        with open(cache_filename, 'r', encoding="utf-8") as file:
            return json.loads(file.read())
    except:
        return {}

def write_json(cache_filename, dict):
    dump_file = json.dumps(dict, indent = 4)
    with open(cache_filename, 'w') as file: 
        file.write(dump_file) 

# def get_request_url(list):
#     r = requests.get('https://open.tiktokapis.com/v2/user/info')
#     #url = f"https://open.tiktokapis.com/v2/user/info/5b17fb869d9cf530dd9a6b45cf9228bf"
#     HEADERS = {{'authorization': 'Bearer' + API_KEY = "5b17fb869d9cf530dd9a6b45cf9228bf"}}
