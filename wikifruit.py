import json
import unittest
import os
import requests
import re 
from xml.sax import parseString
from bs4 import BeautifulSoup


def get_request_url():
    url = 'https://simple.wikipedia.org/wiki/List_of_fruits'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    pay = soup.find_all('li')
    for li in pay:
        content = li.find('a')
        for item in content:
            if str(item).isalpha():
                print(item)

# url = 'https://simple.wikipedia.org/wiki/List_of_fruits'
# response = requests.get(url)
# soup = BeautifulSoup(response.content,'html.parser')
# #var = 'component page-object text'
# pay = soup.find_all('ul', class_= "mw-body-content mw-content-ltr")
# #listofpay = []
# #print(soup)
# # for tag in pay:
# #     print(tag.text)
# # something = tag.find_all('p')
# # if len(something) != 0:
# #listofpay.append(something[0].text)
# for data in pay: 
#    print(data)


def main():
    get_request_url()

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
