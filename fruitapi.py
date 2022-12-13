import plotly.express as px
import json
import unittest
import os
import requests
import matplotlib.pyplot as plt
import re 
from xml.sax import parseString
from bs4 import BeautifulSoup
import statistics
from statistics import mean
import sqlite3
from fractions import Fraction as f
import wikifruit

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


def get_plot(data,xlabel,ylabel,title):
    x = list(data.keys())
    y = list(data.values())
    fig = px.bar(x=x,y=y, labels = {'x': xlabel, 'y':ylabel}, title = title)
    fig.show()
    
def get_get_plot(data):
    x = list(data.keys())
    y = list(data.values())
    fig = px.bar(x=x, y=y, labels = {'x': "Calculated Mean", 'y':"Average Mean for Nutritional Facts"}, title = "Finding the Mean For Three Nutritional Facts")
    fig.show()
    print(data)    

def get_request_url(fruit_name):
    r = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit_name}")
    return r.json()

def mean(): 
    graph_dict = {}
    calories = [96, 60, 50, 50, 46, 61]
    protein = [1, 0.82, 0.54, 1, 0.7, 1.1]
    sugar = [17.2, 13.7, 9.85, 8, 9.92, 9]
    x = statistics.mean(calories)
    y = statistics.mean(protein)
    f = statistics.mean(sugar)
    graph_dict['calories']= x
    graph_dict['protein'] = y
    graph_dict['sugar'] = f
    return graph_dict

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


    apricot = get_request_url('apricot') 
    avocado = get_request_url('avacado') 
    blackberry = get_request_url('blackberry') 
    blueberry = get_request_url('blueberry') 
    cranberry = get_request_url('cranberry') 
    grape = get_request_url('grape') 
    banana = get_request_url('banana') 
    mango = get_request_url('mango') 
    pineapple = get_request_url('pineapple')
    cherry = get_request_url('cherry')
    plum = get_request_url('plum')
    kiwi = get_request_url('kiwi')
    lime = get_request_url('lime') 
    lime2 = get_info(lime)
    mango = get_request_url('mango') 
    mango2 = get_info(mango)
    orange = get_request_url('orange') 
    orange2 = get_info(orange)
    peach = get_request_url('peach') 
    peach2 = get_info(peach)
    pear = get_request_url('pear') 
    pear2 = get_info(pear)
    pineapple = get_request_url('pineapple') 
    pineapple2 = get_info(pineapple)
    plum = get_request_url('plum') 
    plum2 = get_info(plum)
    raspberry = get_request_url('raspberry') 
    raspberry2 = get_info(raspberry)
    strawberry = get_request_url('strawberry') 
    strawberry2 = get_info(strawberry)
    tomato = get_request_url('tomato') 
    tomato2 = get_info(tomato)
    watermelon = get_request_url('watermelon')
    watermelon2 = get_info(watermelon) 
    apricot2 = get_info(apricot)
    avocado2 = get_info(avocado)
    blackberry2 = get_info(blackberry)
    blueberry2 = get_info(blueberry)
    cranberry2 = get_info(cranberry)
    apple = get_request_url('apple')
    apple2 = get_info(apple)
    lemon = get_request_url('lemon')
    lemon2 = get_info(lemon)

    grape2 = get_info(grape)
    banana2 = get_info(banana)
    mango2 = get_info(mango) 
    pineapple2 = get_info(pineapple)
    cherry2 = get_info(cherry)
    plum2 = get_info(plum)
    kiwi2 = get_info(kiwi)
    list_of_fruits = [apple2,apricot2,avocado2,banana2,blackberry2,blueberry2,cherry2,cranberry2,grape2,kiwi2,lemon2,lime2,mango2,orange2,peach2,pear2,pineapple2,plum2,raspberry2,strawberry2,tomato2,watermelon2]
    list_of_fruits2 = [apple,apricot,avocado,banana,blackberry,blueberry,cherry,cranberry,grape,kiwi,lemon,lime,mango,orange,peach,pear,pineapple,plum,raspberry,strawberry,tomato,watermelon]

    print(get_calories(list_of_fruits))
    print(get_protein(list_of_fruits))
    print(get_sugar(list_of_fruits))

    for item in list_of_fruits2:
        print(get_info(item))

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
    # for item in list_of_nutrition:
    #     get_plot(item)
    # print(get_plot)
    get_plot(data1, xlabel='Fruit', ylabel='Calories', title = 'Find Calories')
    get_plot(data2, xlabel='Fruit', ylabel='Protein', title = 'Find Protein')
    get_plot(data3, xlabel='Fruit', ylabel='Sugar', title = 'Find Sugar')
    

    somethings = mean()
    get_get_plot(somethings)

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
