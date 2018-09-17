import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict

import os
os.environ["HTTPS_PROXY"] = "https://ipg_2014037:Divanshu79@192.168.1.107:3128"


link = 'https://www.worldfootball.net'
half_link = [('2023 Guinea', '/players/afrika-cup-2023-guinea/'), ('2021 Elfenbeinküste', '/players/afrika-cup-2021-elfenbeinkueste/'), ('2019 Kamerun', '/players/afrika-cup-2019-kamerun/'), ('2017 Gabun', '/players/afrika-cup-2017-gabun/'), ('2015 Equatorial Guinea', '/players/afrika-cup-2015-aequatorialguinea/'), ('2013 Südafrika', '/players/afrika-cup-2013-suedafrika/'), ('2012 Gabun und Äquatorialg.', '/players/afrika-cup-2012-gabun-und-aequatorialg/'), ('2010 Angola', '/players/afrika-cup-2010-angola/'), ('2008 Ghana', '/players/afrika-cup-2008-in-ghana/'), ('2006 Egypt', '/players/afrika-cup-2006-in-aegypten/'), ('2004 Tunisia', '/players/afrika-cup-2004-in-tunesien/'), ('2002 Mali', '/players/afrika-cup-2002-in-mali/'), ('2000 Ghana/Nigeria', '/players/afrika-cup-2000-in-ghana-nigeria/'), ('1998 Burkina Faso', '/players/afrika-cup-1998-in-burkina-faso/'), ('1996 South Africa', '/players/afrika-cup-1996-in-suedafrika/'), ('1994 Tunisia', '/players/afrika-cup-1994-in-tunesien/'), ('1992 Senegal', '/players/afrika-cup-1992-im-senegal/'), ('1990 Algeria', '/players/afrika-cup-1990-in-algerien/'), ('1988 Morocco', '/players/afrika-cup-1988-in-marokko/'), ('1986 Egypt', '/players/afrika-cup-1986-in-aegypten/'), ('1984 Ivory Coast', '/players/afrika-cup-1984-in-der-elfenbeinkueste/'), ('1982 Libya', '/players/afrika-cup-1982-in-libyen/'), ('1980 Nigeria', '/players/afrika-cup-1980-in-nigeria/'), ('1978 Ghana', '/players/afrika-cup-1978-in-ghana/'), ('1976 Ethiopia', '/players/afrika-cup-1976-in-aethiopien/'), ('1974 Egypt', '/players/afrika-cup-1974-in-aegypten/'), ('1972 Cameroon', '/players/afrika-cup-1972-in-kamerun/'), ('1970 Sudan', '/players/afrika-cup-1970-im-sudan/'), ('1968 Ethiopia', '/players/afrika-cup-1968-in-aethiopien/'), ('1965 Tunisia', '/players/afrika-cup-1965-in-tunesien/'), ('1963 Ghana', '/players/afrika-cup-1963-in-ghana/'), ('1962 Ethiopia', '/players/afrika-cup-1962-in-aethiopien/'), ('1959 Egypt', '/players/afrika-cup-1959-in-aegypten/'), ('1957 Sudan', '/players/afrika-cup-1957-im-sudan/')]
# half_link = half_link[3:]
data = defaultdict(list)
t = 1
for o in half_link:
    r = requests.get(link+o[1])
    soup = BeautifulSoup(r.content, "html.parser")
    tr = soup.find('table', {'class': 'standard_tabelle', 'cellpadding':'3'})
    # tr = soup.find('tbody')
    td = tr.find_all('td')
    for j in range(len(td)):
        i = j%8
        if i == 0:
            img = td[j].find('img')
            src = img.get('src')
            data['team_flag'].append(src)
        elif i == 1:
            data['year'].append(o[0][:4])
            data['host'].append(o[0][5:])
            data['id'].append(t)
            t += 1
            text = td[j].text
            data['team'].append(text)
        elif i == 2:
            img1 = td[j].find('img')
            src1 = img1.get('src')
            data['nation_flag'].append(src1)
        elif i == 3:
            link2 = td[j].find('a')
            data['info'].append(link2.get('href'))
        elif i == 4:
            link3 = td[j].find('a')
            data['match'].append(link3.get('href'))
# print(data['team'])


df = pd.DataFrame(data)
df.to_csv('team_info.csv', sep=',', index=False)


