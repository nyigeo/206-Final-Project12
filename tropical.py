import json
import unittest
import os
import requests
import re 
from xml.sax import parseString
from bs4 import BeautifulSoup


def get_request_url(tropicalfruit):
    #HEADERS = {'authorization': 'Bearer ' + API_KEY}
    #dd
    r = requests.get(f'http://api.tropicalfruitandveg.com/tfvjsonapi.php?tfvitem={tropicalfruit}')
    # most healthy: cherry, grapefruit
    # most unhealthy: bananas, mangoes, pineapples 
    #url = f"https://open.tiktokapis.com/v2/user/info/5b17fb869d9cf530dd9a6b45cf9228bf"
   # HEADERS = {'authorization': 'Bearer ' + API_KEY}
    print(r.text)
def tropical_fruit(): 
    #create a dictionary 
    pass
def main():
    get_request_url('mango')
    pass

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)

