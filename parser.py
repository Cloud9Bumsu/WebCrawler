## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os


## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://media.dongguk.edu/multilive/portal/index/main.php?dirnm=media_sin&filenm=media&s_kind1=all&s_kind2=1&s_kind3=subject&s_word=&num_per_page=50&page=1', verify=False)
req.encoding=
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'p > b > a > font'
    )

data = {}

for title in my_titles:
    print(title.text)
    data[title.text] = title.text

with open(os.path.join(BASE_DIR, 'result.json'),'w+') as json_file:
    json.dump(data,json_file)
