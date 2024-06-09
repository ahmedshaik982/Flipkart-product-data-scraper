# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 09:30:06 2024

@author: HP
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
})

url = 'https://www.flipkart.com/gaming/gaming-consoles/pr?sid=4rr,x1m&otracker=nmenu_sub_Sports%2C%20Books%20%26%20More_0_Gaming%20Consoles&otracker=nmenu_sub_Sports%2C%20Books%20%26%20More_0_Gaming%20Consoles'
response = session.get(url)
response

soup = BeautifulSoup(response.text, 'lxml')
s = 0
products_list = []

def get_text_or_default(element, selector, class_name, default='NA'):
    try:
        return element.find(selector, class_name).text
    except:
        return default

for k in range(59):
    product_card = soup.find_all('div', class_ = 'slAVV4')
    for a in product_card:
        title = get_text_or_default(a, 'a', 'wjcEIp')
        rating = get_text_or_default(a, 'div', 'XQDdHH')
        price = get_text_or_default(a, 'div', 'Nx9bqj')
        products_list.append([title,rating, price])
        
    url_cont = soup.find('a', class_ = '_9QVEpD').get('href')
    url = 'https://www.flipkart.com' + url_cont
    response = session.get(url) 
    soup = BeautifulSoup(response.text, 'lxml')
    print(s)
    s = s+1

len(products_list)
df = pd.DataFrame(products_list, columns=["Title", "Rating", "Price"])
df.to_csv('flipkart_products.csv')