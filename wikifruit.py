import json
import unittest
import os
import requests
import re 
import sqlite3
from xml.sax import parseString
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def found_fruits():
    url = 'https://snaped.fns.usda.gov/seasonal-produce-guide'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    fruits = soup.find('div',{'class':'paragraph paragraph--type-view paragraph--view-mode-default'})
    season_list = ['Spring', 'Summer', 'Winter', 'Fall','&']
    fruit_list = []
    for fruit in fruits.text.split():
        if fruit not in season_list:
         fruit_list.append(fruit)
    print(fruit_list)
    return fruit_list 

def pie_chart(fruit_list): 
   Bananas = fruit_list.count('Bananas')
   Limes = fruit_list.count('Limes')
   Mushrooms = fruit_list.count('Mushrooms')
   Onions = fruit_list.count('Onions')
   x = [Bananas, Limes, Mushrooms, Onions]
   fig, ax = plt.subplots()
   ax.pie(x, radius=3, center=(4, 4), labels = ['Bananas','Limes', 'Mushrooms', 'Onions'],shadow=True,startangle=90)
   ax.axis('equal')
   plt.tight_layout()
   plt.show()

def found_season():
    seasons_list = ['Spring', 'Summer', 'Winter', 'Fall']
    return seasons_list 

def found_fruit_season():
    url = 'https://snaped.fns.usda.gov/seasonal-produce-guide'
    response = requests.get(url)
    spring_list = []
    summer_list = []
    fall_list = []
    winter_list = []
    soup = BeautifulSoup(response.content,'html.parser')
    spring_fruit = soup.find('div',{'class':'seasonal-produce--landing-season spring'}).find_all('a')

    for fruit in spring_fruit[1:]:
        spring_list.append(fruit.text)
        print('Spring: ', spring_list)
    fall_fruit = soup.find('div',{'class':'seasonal-produce--landing-season fall'}).find_all('a')
    for fruit in fall_fruit[1:]:
        fall_list.append(fruit.text)
    print('Fall: ', fall_list)

    summer_fruit = soup.find('div',{'class':'seasonal-produce--landing-season summer'}).find_all('a')
    for fruit in summer_fruit[1:]:
        summer_list.append(fruit.text)
    print('Summer: ', summer_list)
    winter_fruit = soup.find('div',{'class':'seasonal-produce--landing-season winter'}).find_all('a')
    for fruit in winter_fruit[1:]:
        winter_list.append(fruit.text)
    print('Winter: ', winter_list)
    return ('Spring: ', spring_list), ('Summer: ', summer_list),('Fall: ', fall_list),('Winter: ', winter_list)

def found_temperature(): 
    temperature_list = ['Celsius', 'Fahrenheit']
    return temperature_list


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_fruits_table(cur, conn, fruit_list):

    cur.execute("DROP TABLE IF EXISTS matchedfruit")
    cur.execute("CREATE TABLE matchedfruit (id INTEGER PRIMARY KEY, FruitName TEXT)")
    for i in range(len(fruit_list)):
        cur.execute("INSERT INTO matchedfruit (id,FruitName) VALUES (?,?)",(i,fruit_list[i]))
    conn.commit()

def create_seasons_table(cur, conn, seasons_list):

    cur.execute("DROP TABLE IF EXISTS matchedseasons")
    cur.execute("CREATE TABLE matchedseasons (id INTEGER PRIMARY KEY, SeasonName TEXT)")
    fruit_count = cur.fetchone()[0]
    count = 1
    id = count 
    for i in range(fruit_count,count + 25):
        cur.execute("INSERT INTO matchedseasons (id,SeasonName) VALUES (?,?)",(i,seasons_list[i])).fetchone()[0]
        id += 1
    conn.commit()

def create_temperature_table(cur, conn, temperature_list):

    cur.execute("DROP TABLE IF EXISTS matchedtemperature")
    cur.execute("CREATE TABLE matchedtemperature (id INTEGER PRIMARY KEY, TemperatureName TEXT)")
    for i in range(len(temperature_list)):
        cur.execute("INSERT INTO matchedtemperature (id,TemperatureName) VALUES (?,?)",(i,temperature_list[i]))
    conn.commit()

def main():
    something = found_fruits()
    something2 = found_season()
    something3 = found_temperature()
    cur, conn = setUpDatabase('fruits.db')
    found_fruit_season()
    create_fruits_table(cur, conn, something)
    create_seasons_table(cur, conn, something2)
    create_temperature_table(cur, conn, something3)
    found_season()
    pie_chart(something)

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
