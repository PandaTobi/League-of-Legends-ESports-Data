###GETTING THE DATA AND STORING IT
from bs4 import BeautifulSoup
import csv
import urllib.request as request

data = []

req = request.Request(
        "https://gol.gg/players/list/season-S10/split-Spring/tournament-ALL/position-ALL/week-ALL/", 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
)

response = request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, features="lxml")  

table = soup.find("table", attrs={"class": 
    "table_list playerslist tablesaw trhover"})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    i = [ele for ele in cols if ele]
    
    with open ("league_pro_play_data.csv", 'a', encoding="utf-8") as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(i[0:11])

