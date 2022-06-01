import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

news_list = []

for offset in range(0, 1001, 10):
    reuters = 'https://www.reuters.com/site-search/?query=bitcoin&offset=' + str(offset)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(reuters)

    page_source = driver.page_source
    search_soup = BeautifulSoup(page_source, 'lxml')
    results = search_soup.find_all('a', class_ = 'text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_6__1qUJ5 heading__base__2T28j heading__heading_6__RtD9P media-story-card__heading__eqhp9')

    for result in results:
        link = "https://www.reuters.com" + result.get('href')
        news_html = requests.get(link).text
        news_soup = BeautifulSoup(news_html, 'lxml')

        news_dictionary = {}

        # extract news_date
        news_date = news_soup.find('span', class_ = 'date-line__date__23Ge-')
        news_dictionary["date"] = news_date.text

        # extract news_headline
        news_headline = news_soup.find('h1', class_ = 'text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_2__1K_hh heading__base__2T28j heading__heading_2__3Fcw5')
        news_dictionary["headline"] = news_headline.text

        # extract news_content
        # WARNING : catch for an error here !!!
        news_content = ''
        paragraphs = news_soup.find_all('p', class_ = 'text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__base__22dCE body__large_body__FV5_X article-body__element__2p5pI')
        for paragraph in paragraphs:
            news_content += " "
            news_content += paragraph
        news_dictionary["content"] = news_content

        # extract news_source
        news_source = 'Reuters'
        news_dictionary["source"] = news_source

        # extract news_url
        news_url = link
        news_dictionary["url"] = news_url

        # add the completed dictionary to the list
        news_list.append(news_dictionary)

# code for converting list of news dictionaries into csv format start here

news_df = pd.DataFrame(news_list)
news_df.to_csv('reuters_news.csv', index=False)