###RUN THIS FIRST
from bs4 import BeautifulSoup
import urllib.request as urllib2

f = open("links.txt", "a")

"""
Creating a file of links to be processed later.
"""
html_page = urllib2.urlopen("https://gol.gg/players/list/season-S10/split-Spring/tournament-ALL/position-ALL/week-ALL/")
soup = BeautifulSoup(html_page, features="lxml")
for link in soup.find_all('a'):
    if str(link.get('href')).startswith("./player-stats/"):
        f.write(str(link.get('href')).strip('.'))
        f.write("\n")
    
f.close()
