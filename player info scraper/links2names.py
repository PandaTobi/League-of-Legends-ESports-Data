###RUN THIS SECOND

from bs4 import BeautifulSoup
import urllib.request as request

f = open('links.txt', "r")

index = 0
for i in f:
    link = open('linksNames.txt', "a")
    names = open('names.txt', "a")
    
    response = request.urlopen('https://gol.gg/players{}'.format(i))
    html = response.read()
    soup = BeautifulSoup(html, features="lxml")
    
    name = soup.find("h1")
    print(type(i))
    print("yessir: {}".format(index))
    
    #Basically, in this code I'm extracting all the names of the players
    #within the link.txt file, for the purpose of the future mini search
    #engine I've made in retrieve_player_data.py.
    names.write(name.text)
    names.write("\n")
    link.write(i.strip() + "#{}".format(name.text.lower().strip()))
    link.write("\n")
    
    index += 1       
    
    link.close()
