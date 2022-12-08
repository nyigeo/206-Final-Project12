import json
import unittest
import os
import requests
import re 
import sqlite3
from xml.sax import parseString
from bs4 import BeautifulSoup

def found_fruits():
   url = 'https://snaped.fns.usda.gov/seasonal-produce-guide'
   response = requests.get(url)
   soup = BeautifulSoup(response.content,'html.parser')
   #var = 'component page-object text'
   fruits = soup.find('div',{'class':'paragraph paragraph--type-view paragraph--view-mode-default'})

   season_list = ['Spring', 'Summer', 'Winter', 'Fall','&']
   
   fruit_list = []
   for fruit in fruits.text.split():
        if fruit not in season_list:
            fruit_list.append(fruit)
   return fruit_list
#    letter_fruit = []
#    for fruit in fruit_list:

    
    
    

def found_season():
#    url = 'https://snaped.fns.usda.gov/seasonal-produce-guide'
#    response = requests.get(url)
#    soup = BeautifulSoup(response.content,'html.parser')
#    response = requests.get(url)
#    soup = BeautifulSoup(response.content,'html.parser')
 seasons_list = ['Spring', 'Summer', 'Winter', 'Fall']
#    seasons = soup.find('div',{'class':'paragraph paragraph--type-view paragraph--view-mode-default'}).find('a').text
# #    season_text = list(seasons.descendants)
#    seasons_list.append(seasons)
    # for season in seasons.text.split():
    #      if 'Spring' 'Summer' 'Winter' 'Fall':
 return seasons_list 

   

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Creates list of species ID's and numbers
def create_fruits_table(cur, conn, fruit_list):

    cur.execute("DROP TABLE IF EXISTS matchedfruit")
    cur.execute("CREATE TABLE matchedfruit (id INTEGER PRIMARY KEY, FruitName TEXT)")
    for i in range(len(fruit_list)):
        cur.execute("INSERT INTO matchedfruit (id,FruitName) VALUES (?,?)",(i,fruit_list[i]))
    conn.commit()
def create_seasons_table(cur, conn, seasons_list):

    cur.execute("DROP TABLE IF EXISTS matchedseasons")
    cur.execute("CREATE TABLE matchedseasons (id INTEGER PRIMARY KEY, SeasonName TEXT)")
    for i in range(len(seasons_list)):
        cur.execute("INSERT INTO matchedseasons (id,SeasonName) VALUES (?,?)",(i,seasons_list[i]))
    conn.commit()



def main():
    # SETUP DATABASE AND TABLE
    something = found_fruits()
    something2 = found_season()
    cur, conn = setUpDatabase('fruits.db')
    create_fruits_table(cur, conn, something)
    create_seasons_table(cur, conn, something2)
   

    # create_patients_table(cur, conn)
   #  add_fluffle(cur, conn)
   #  add_pets_from_json('pets.json', cur, conn)
   #  ls = (non_aggressive_pets(10, cur, conn))
   #  print(ls)

    
    
if __name__ == "__main__":
     main()
     unittest.main(verbosity = 2)
