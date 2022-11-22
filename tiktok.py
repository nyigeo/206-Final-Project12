# List who you have worked with on this project: Nyia George, Isabel Lopez, Caria Blevins 
import json
import unittest
import os
import requests
import re 
from xml.sax import parseString
from bs4 import BeautifulSoup

#API_KEY = "5b17fb869d9cf530dd9a6b45cf9228bf"
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

def get_request_url(fruit_name):
    #HEADERS = {'authorization': 'Bearer ' + API_KEY}
    #dd
    r = requests.get(f'https://www.fruityvice.com/api/fruit/{fruit_name}')
    # most healthy: cherry, grapefruit
    # most unhealthy: bananas, mangoes, pineapples 
    #url = f"https://open.tiktokapis.com/v2/user/info/5b17fb869d9cf530dd9a6b45cf9228bf"
   # HEADERS = {'authorization': 'Bearer ' + API_KEY}
    print(r.text)

# url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

# querystring = {"prefix":"chicken soup"}

# headers = {
# 	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
# 	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)


# def get_data_using_cache(list, cache_filename):
#     request_url =  get_request_url(list)
#     dictionary = read_json(cache_filename)
#     if request_url in dictionary:
#         print("Using cache for {}".format(list))
#         return dictionary[request_url]
#     else: 
#         print("Fetching data for {}".format(list))
#         try: 
#             url = requests.get(request_url).text
#             book_info = json.loads(url)
#             if book_info["status"] == "OK":
#                 dictionary[request_url] = book_info["results"]
#                 write_json(cache_filename, dictionary)
#                 return dictionary.get(request_url)
#             else: 
#                 print("No list found for list name provided.")
#                 return None 
#         except:
#             print("Exception")
#             return None

def display_fruit_name():
    #displays the fruit name 
    pass
def display_fruit_family(): 
    #displays the fruit family 
    pass
def display_fruit_genus_(): 
    #displays the fruit genus 
    pass 
def display_fruit_order():
    #display the fruit order 
    pass
def main():
    get_request_url('banana') 
    get_request_url('mango') 
    get_request_url('pineapple')
    get_request_url('cherry')
    get_request_url('plum')
    get_request_url('kiwi')
    pass

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
