# List who you have worked with on this project: Nyia George, Isabel Lopez, Caria Blevins 
import json
import unittest
import os
import requests
import re 
from xml.sax import parseString
from bs4 import BeautifulSoup

API_KEY = "5b17fb869d9cf530dd9a6b45cf9228bf"
# HEADERS = {'Authorization': 'Bearer {}'.format(API_KEY),
#            'User-Agent': 'YelpEventAnalyzer',
#            'From': 'himharis@icloud.com',
#            'Course-Info': 'https://si.umich.edu/programs/courses/507'
# }

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

def get_request_url(r):
    HEADERS = {'authorization': 'Bearer ' + API_KEY}
    r = requests.get('https://open.tiktokapis.com/v2/user/info', headers = HEADERS)
    #url = f"https://open.tiktokapis.com/v2/user/info/5b17fb869d9cf530dd9a6b45cf9228bf"
   # HEADERS = {'authorization': 'Bearer ' + API_KEY}
    print(r.text)

def get_data_using_cache(list, cache_filename):
    request_url =  get_request_url(list)
    dictionary = read_json(cache_filename)
    if request_url in dictionary:
        print("Using cache for {}".format(list))
        return dictionary[request_url]
    else: 
        print("Fetching data for {}".format(list))
        try: 
            url = requests.get(request_url).text
            book_info = json.loads(url)
            if book_info["status"] == "OK":
                dictionary[request_url] = book_info["results"]
                write_json(cache_filename, dictionary)
                return dictionary.get(request_url)
            else: 
                print("No list found for list name provided.")
                return None 
        except:
            print("Exception")
            return None

def display_name():
    #displays the username 
    pass
def follower_count(): 
    #displays the user's followers count 
    pass
def likes_count(): 
    #shares the total number of likes received by the user across all of their videos 
    pass 
def main():
    pass

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
