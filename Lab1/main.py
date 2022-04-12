#This program we need to cheack how requests are working!
# >> Usual programm created for fun.

import requests
import re
from bs4 import BeautifulSoup
url = input();
yandex_url = r'https://yandex.ru/images/search?source=collections&rpt=imageview&url='

soup = BeautifulSoup(requests.get(yandex_url+url).text, 'lxml')
similar = soup.find('section',class_='CbirTags').find_all('span', class_='Button2-Text')
for i in similar:
    a=str(i)
    b=re.findall(r'>(.*)<', a)[0]
    print(b)
