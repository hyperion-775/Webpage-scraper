import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from termcolor import colored

x = input("What webpage do you want scraped?")
page=requests.get(x)
#page=requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)

soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())
print("----")
html=list(soup.children)[2]


print("This is all HTML kids")
print(list(html.children))
print("-------------------------")
head=list(html.children)[1]
title=list(head.children)[1]
print(title)
print(title.get_text())
print("----")
body=list(html.children)[3]

print(list(body.children)[1])
print("----")
p=list(body.children)[1]
print(p.get_text())
soup.find_all()
