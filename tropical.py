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
#     print(r.text)
    return r.text 

def get_request_url2(all):
    r = requests.get(f'https://tropicalfruitandveg.com/api/tfvjsonapi.php?search={all}')
    # most healthy: cherry, grapefruit
    # most unhealthy: bananas, mangoes, pineapples
    print(r.text)
    # return r.text
    
 def get_rainfall(avocado):
    # fruit_list = ['mango', 'dragon fruit', 'avocado', 'ginger', 'jackfruit']
    avocado_results = get_request_url(avocado)
    avocado_dict = json.loads(avocado_results) 
    climate_info = avocado_dict['results'][0]['climate']
    if 'rainfall' in climate_info:
        print(True)
        # write regex statement here for mango 
        if re.search(r"rainfall.*\d cm",climate_info) != None:
            print(re.search(r"rainfall.*\d cm",climate_info))
    else: 
        print(False)
    # print(fruit_list)
    print(climate_info)
    # print(avocado_dict)
    # print(avocado_results)

# 1) generate regex for meters 
# 2) finish getting all fruits from the list 
# 3) how to convert the list of headers into a list of fruits (currently a list of dictionaries)
# 4) list comprehension (python) or a for loop 
        

def tropical_fruit(): 
    #create a dictionary 
    pass
def main():
    get_request_url('mango')
    # get_request_url2('all')
    # get_rainfall('dragon fruit')
    get_rainfall('avocado')
    # get_request_url('mango')
    # get_request_url2('')
    pass

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)

