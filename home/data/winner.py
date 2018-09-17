import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict

import os
os.environ["HTTPS_PROXY"] = "https://ipg_2014037:Divanshu79@192.168.1.107:3128"

link = 'https://www.worldfootball.net/winner/afrika-cup/'
r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
tr = soup.find('table', {'class': 'standard_tabelle', 'cellpadding':'3'})
td = tr.find_all('td')
data = defaultdict(list)
for j in range(len(td)):
    i = j%5
    if i == 0:
        txt = td[j].text
        txt = txt[1:5]
        data['year'].append(txt)
    elif i == 2:
        text = td[j].text
        data['team'].append(text)
df = pd.DataFrame(data)
df.to_csv('winners.csv', sep=',', index=False)
