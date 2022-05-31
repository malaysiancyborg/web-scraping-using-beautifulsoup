from lib2to3.pgen2 import driver
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

offset = 0

reuters = 'https://www.reuters.com/site-search/?query=bitcoin&offset=0'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(reuters)

page_source = driver.page_source

search_soup = BeautifulSoup(page_source, 'lxml')

result = search_soup.find('a', class_ = 'text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_6__1qUJ5 heading__base__2T28j heading__heading_6__RtD9P media-story-card__heading__eqhp9')
news_url = "https://www.reuters.com" + result.get('href')
print(news_url)

news_html = requests.get(news_url).text
news_soup = BeautifulSoup(news_html, 'html.parser')
news_title = news_soup.find('h1', {'class' : 'text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_2__1K_hh heading__base__2T28j heading__heading_2__3Fcw5'})
print(news_title.text)

