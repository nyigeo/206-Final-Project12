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

   season_list = ['Spring', 'Summer', 'Winter', 'Fall']
   fruit_list = []
   for fruit in fruits.text.split():
        if fruit not in season_list:
            fruit_list.append(fruit)
   print(fruit_list)



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



def main():
    # SETUP DATABASE AND TABLE
    something = found_fruits()
    cur, conn = setUpDatabase('fruits.db')
    create_fruits_table(cur, conn, something)
   

   #  create_patients_table(cur, conn)
   #  add_fluffle(cur, conn)
   #  add_pets_from_json('pets.json', cur, conn)
   #  ls = (non_aggressive_pets(10, cur, conn))
   #  print(ls)

    
    
if __name__ == "__main__":
     main()
     unittest.main(verbosity = 2)
