import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.biostathandbook.com/index.html')

#### get the index page so we can make a list of all the topics to scrap
soup = BeautifulSoup(driver.page_source, 'html')
## the index is located at the following
ind_=soup.find_all("p", class_="outlinelink")
## we got our index urls lets write a loop to visit these pages and store the bsoup object
ind_urls = [i.a['href'] for i in ind_ if len(i.text.strip()) > 1] ### remove empty urls 

### run this loop, your proxy google browser will make a loop visit to urls in the list and get the soup objects
soups =[]
for i in ind_urls:
	driver.get(i)
	tsoup=BeautifulSoup(driver.page_source, 'html')
	soups.append(tsoup)
##### write the content to a file 
with open('BIO_STAT.txt', 'w') as f:
	for soup in soups:
		test = soup.find_all('div', id ='content') ### all the content is found here
		print test[0].text.rstrip()
		f.write(test[0].text.encode('utf-8').rstrip())

