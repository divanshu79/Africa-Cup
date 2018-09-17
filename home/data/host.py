import requests
from bs4 import BeautifulSoup
import pandas as pd

import os
os.environ["HTTPS_PROXY"] = "https://ipg_2014037:Divanshu79@192.168.1.107:3128"


link = 'https://www.worldfootball.net'
k = '/players/afrika-cup-1957-im-sudan/'
r = requests.get(link+k)
soup = BeautifulSoup(r.content, "html.parser")
genre_div = soup.find_all('select', {'name': 'saison'})
data = genre_div[0].find_all('option')
data1 = []
host = {'year':[], 'host':[]}
for i in data:
    data1.append((i.text, i.get('value')))
    p = i.text
    year = p[:4]
    host1 = p[5:]
    host['year'].append(year)
    host['host'].append(host1)
print(data1)
columns = ['year', 'host']
df = pd.DataFrame(host, columns=columns)
df.to_csv('host.csv', sep=',', columns=columns, index=False)

