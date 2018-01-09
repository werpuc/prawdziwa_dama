import sys
import re
import requests
import time
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_url(word, start, end, language):
    pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}")
    assert pattern.match(start)
    assert pattern.match(end)
    assert end > start
    url = u'https://twitter.com/search?q='+word+'%20since%3A'+start+'%20until%3A'+end+'&l='+language+'&src=typd&f=tweets'
    return url

def main(word, start_date, end_date, language):
    url = get_url(word, start_date, end_date, language)
   
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(1)
    body = browser.find_element_by_tag_name('body')
    for _ in range(10):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    tweets = list()
    for date in browser.find_elements_by_class_name("content"):
        #soup = BeautifulSoup(date.get_attribute('outerHTML'), 'lxml')
        soup = BeautifulSoup(date.get_attribute('outerHTML'))
        tweet = soup.find("p", class_="tweet-text").text
        tm = int(soup.find("span", class_="_timestamp").get('data-time')) - 3600
        date = datetime.datetime.fromtimestamp(tm).strftime('%Y-%m-%d %H:%M:%S')
        tweets.append((date, tm, tweet))

    browser.close()

    df = pd.DataFrame(tweets)
    df.columns = ['when', 'timestamp', 'tweet']
    df['length'] = len(df['tweet'])
    for i in range(len(df)):
        df['length'][i] = len(df['tweet'][i])
    df.when = pd.to_datetime(df.when)
    # df['time'] = df['when'].dt.time
    # df['date'] = df['when'].dt.date
    df['timestamp'] = df['timestamp'].astype(str).astype(int)
    df['time_s'] = df['timestamp']%86400

    length_mean = int(df.length.mean())
    length_median = int(df.length.median())
    length_time_corr = df.time_s.corr(df.length)

    print("Srednia dlugosc tweeta :", length_mean)
    print("Mediana dlugosci tweeta :", length_median)
    print("Korelacja dlugosc tweeta i czasu publikacji:", length_time_corr)    

if __name__ == "__main__":
    if len(sys.argv)<4 :
        print('Some arguments are missing.')
        print('Please provide word, start date, end date and, if you wish, language (polish default).')
    else:
        word = sys.argv[1]
        start_date = sys.argv[2]
        end_date = sys.argv[3]
        language = sys.argv[4] if len(sys.argv)>4 else 'pl'

    main(word, start_date, end_date, language)

