import json
import unittest
import os
import requests
import re 
import sqlite3
from xml.sax import parseString
from bs4 import BeautifulSoup

def found_fruits():
   url = 'https://simple.wikipedia.org/wiki/List_of_fruits'
   response = requests.get(url)
   soup = BeautifulSoup(response.content,'html.parser')
   #var = 'component page-object text'
   fruits = soup.find('div',{'class':'div-col'}).find('ul')
   text = list(fruits.descendants)
   # print(text)
   fruitlist = []
   for i in range(2,len(text)):
      if '\n' not in text[i].text and text[i].text not in fruitlist and '(' not in text[i].text and ')' not in text[i].text:
         fruitlist.append(text[i].text)
   return fruitlist



def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Creates list of species ID's and numbers
def create_fruits_table(cur, conn, fruitlist):

    cur.execute("DROP TABLE IF EXISTS matchedfruit")
    cur.execute("CREATE TABLE matchedfruit (id INTEGER PRIMARY KEY, FruitName TEXT)")
    for i in range(len(fruitlist)):
        cur.execute("INSERT INTO matchedfruit (id,FruitName) VALUES (?,?)",(i,fruitlist[i]))
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
