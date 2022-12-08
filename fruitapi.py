# List who you have worked with on this project: Nyia George, Isabel Lopez, Caria Blevins 
import json
import unittest
import os
import requests
import plotly.express as px
import matplotlib.pyplot as plt
import re 
import sqlite3
from xml.sax import parseString
from bs4 import BeautifulSoup
import wikifruit
# from get_matches import wikifruit.py 

#API_KEY = "5b17fb869d9cf530dd9a6b45cf9228bf"
# HEADERS = {'Authorization': 'Bearer {}'.format(API_KEY),
#            'User-Agent': 'YelpEventAnalyzer',
#            'From': 'himharis@icloud.com',
#            'Course-Info': 'https://si.umich.edu/programs/courses/507'
# }

print(wikifruit.found_fruits())
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

def get_info(fruit):
    fruit_info = {}
    for i,j in fruit.items():
        if i == 'name':
            nutrition = {}
            for key,value in fruit['nutritions'].items():
                if key == 'protein':
                    nutrition[key] = value
                elif key == 'calories':
                    nutrition[key] = value
                elif key == 'sugar':
                    nutrition[key] = value
            fruit_info[j] = nutrition  
    return fruit_info
def get_calories(list_of_fruits):
    
    dict_fruits = {}
    for fruit in list_of_fruits:
        for key,value in fruit.items():
            for i,j in value.items():
                if i == 'calories':
                    dict_fruits[key] = j
    return dict_fruits
def get_protein(list_of_fruits):
    dict_fruits = {}
    for fruit in list_of_fruits:
        for key,value in fruit.items():
            for i,j in value.items():
                if i == 'protein':
                    dict_fruits[key] = j
    return dict_fruits
def get_sugar(list_of_fruits):
    dict_fruits = {}
    for fruit in list_of_fruits:
        for key,value in fruit.items():
            for i,j in value.items():
                if i == 'sugar':
                    dict_fruits[key] = j
    return dict_fruits




def get_plot(data):
    x = list(data.keys())
    y = list(data.values())
    # data = px.data.gapminder().query("co == 'Canada'")
    fig = px.bar(x=x,y=y)
    fig.show()

        
        
    # if fruit['nutritions'].keys() == 'protein':
    #     protein = {'protein': fruit['nutritions']['protein']}
    #     fruit_info.update(protein) 

    # elif fruit['nutritions'].keys() == 'calories':
    #     calories = {'calories': fruit['nutritions']['calories']}
    #     fruit_info.update(calories)
        
    # elif fruit['nutritions'].keys() == 'sugar':
    #     sugar = {'sugar': fruit['nutritions']['sugar']}
    #     fruit_info.update(sugar)

    # return fruit_info

def get_request_url(fruit_name):
    #HEADERS = {'authorization': 'Bearer ' + API_KEY}
    #dd
    r = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit_name}")
    # most healthy: cherry, grapefruit
    # most unhealthy: bananas, mangoes, pineapples 
    #url = f"https://open.tiktokapis.com/v2/user/info/5b17fb869d9cf530dd9a6b45cf9228bf"
   # HEADERS = {'authorization': 'Bearer ' + API_KEY}
    # print(r.text)
    return r.json()


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


def matched_fruits(list_of_fruits):
    new_fruit_list = []

    fruit_list = wikifruit.found_fruits()
    for fruit in fruit_list:
        for fruit2 in list_of_fruits:
            if fruit2[:4].lower() in fruit.lower():
                new_fruit_list.append(fruit2)

    print(new_fruit_list)
            

def main():
    banana = get_request_url('banana') 
    mango = get_request_url('mango') 
    pineapple = get_request_url('pineapple')
    cherry = get_request_url('cherry')
    plum = get_request_url('plum')
    kiwi = get_request_url('kiwi')
    banana2 = get_info(banana)
    mango2 = get_info(mango) 
    pineapple2 = get_info(pineapple)
    cherry2 = get_info(cherry)
    plum2 = get_info(plum)
    kiwi2 = get_info(kiwi)
    list_of_fruits = [banana2,mango2,pineapple2,cherry2,plum2,kiwi2]
    list_of_fruits_name = [list(item.keys())[0] for item in list_of_fruits]
    matched_fruits(list_of_fruits_name)

    
    print(get_calories(list_of_fruits))
    print(get_protein(list_of_fruits))
    print(get_sugar(list_of_fruits))

    
    print(get_info(cherry))
    print(get_info(mango))
    data1 = get_calories(list_of_fruits)
    data2 = get_protein(list_of_fruits)
    data3 = get_sugar(list_of_fruits)
    list_of_nutrition = [data1,data2,data3]
    for item in list_of_nutrition:
        get_plot(item)
   
    
    pass

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
