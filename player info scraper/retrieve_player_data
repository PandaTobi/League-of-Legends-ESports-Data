# -*- coding: utf-8 -*-

###READ THE README.TXT YOU DONKEY###

from bs4 import BeautifulSoup
import urllib.request as request

f = open('linksNames.txt', "r")

name = input("Player name: ")

"""
Iterating through the links.txt file to check what link corresponds with that 
name then scraping said link for the data table we specified, then printing
it.
"""

for i in f:
    i = i.strip()
    if i.endswith(name.lower()):
        print(i)
        response = request.urlopen('https://gol.gg/players{}'.format(i))
        html = response.read()
        soup = BeautifulSoup(html, features="lxml")
        
        table = soup.find("table", attrs={"class": 
            "table_list"})
    
        name = soup.find("h1")
        
        print("Name: " + name.text)
        
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            i = [ele for ele in cols if ele]
            if i:
                print(i)
                
        break
    
else:
    print("Sorry, that player isn't in our database.")
