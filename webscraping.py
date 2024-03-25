from bs4 import BeautifulSoup
from app.models import *
from time import sleep
from random import randint
import pandas as pd
import requests
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}




games = Games.query.all()

'''
for row in games:
    print("https://www.fnac.pt/SearchResult/ResultList.aspx?SCat=0%211&Search=+"{{row.game_name}}"+&sft=1&sa=0")
''' 

url="https://www.fnac.pt/SearchResult/ResultList.aspx?SCat=0%211&Search=sekiro&sft=1&sa=0"
   
r = requests.get(url, headers=headers)
html_soup = BeautifulSoup(r.content, "html.parser")
price = html_soup.find('strong', class_ = 'userPrice')
name = html_soup.find('a', class_ = 'Article-title js-minifa-title js-Search-hashLink')
link = html_soup.find('a', class_ = 'Article-title js-minifa-title js-Search-hashLink')

name = name.get_text()
game_price = price.get_text().strip().replace('\xa0', '')
game_link = link.get('href')

game_info.append(name)
game_info.append(game_price)
game_info.append(link)
'''
price = game_cost_calendar(price=game_price)
db.session.add(price)
db.session.commit()
'''
    

df = pd.DataFrame({'Game Name': name, 'Price': game_price, 'Link': game_link})
print(df.info())
print(df)

'''
from IPython.core.display import clear_output
start_time = time()requests = 0
requests = 0

for _ in range(5):
    requests += 1
    sleep(randint(1,3))
    current_time = time()
    elapsed_time = current_time - start_time
    print('Request: {}; Frequency {} requests/s'.format(requests/elapsed_time))
clear_output(wait = True)
'''

'''
data = {'a': 1, 'b': 2}
pd.Series(data).to_frame()
'''