from urllib import response
import requests
from bs4 import BeautifulSoup

def scrape_reuters():
    link = 'https://www.reuters.com/site-search/?query=bitcoin&offset=0'
    response = requests.get(link)
    data = response.text
    soup = BeautifulSoup(data, 'html-parser')
    news = soup.find_all("li", {"class":"search-results__item__2oqiX"})
    
    for new in news:
        print(new.text)

scrape_reuters()