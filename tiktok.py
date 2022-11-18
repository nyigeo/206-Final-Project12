import json
import unittest
import os
import requests

API_KEY = "awwg62n4md2eytgf"

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

def get_request_url(list):
    #url = f"https://api.nytimes.com/svc/books/v3/lists/2016-07-10/{list}.json?api-key={API_KEY}" 
    url = f"https://open.tiktokapis.com/v2/user/info/5b17fb869d9cf530dd9a6b45cf9228bf"
    return url 