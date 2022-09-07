import requests
from bs4 import BeautifulSoup as bs
import csv
import time
import subprocess as sp

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import os
from dotenv import load_dotenv

load_dotenv()

chromedriver_autoinstaller.install()

def test_chromedriver():
    options = webdriver.ChromeOptions()
    options.add_argument(os.getenv('PROFILE_PATH'))
    options.add_argument('--profile-directory=Default')
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    # driver.get("https://www.goodreads.com/list/show/1.Best_Books_Ever")
    driver.get("https://www.google.com/")
    title = driver.title
    print(title)
    driver.implicitly_wait(3)

test_chromedriver()

def get_book(url):
    # driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    # print(title)
    driver.implicitly_wait(5)
    stars = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Number of ratings and percentage of total ratings"]')
    
    ratings = []
    for i in range(len(stars)):
        text = stars[i].text
        text = int(text.split()[0].replace(',',''))
        ratings.append(text)

    return ratings
    

# Scraping
# url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
# page = requests.get(url)
# soup = bs(page.content, 'html.parser')
# book_containers = soup.find_all('tr')


# base_url = 'https://www.goodreads.com'
# data = []
# for i in range(len(book_containers)):
#     title = book_containers[i].find('a', class_='bookTitle')
#     author = book_containers[i].find('a', class_='authorName')
#     rating = book_containers[i].find('span', class_='minirating')
#     book_href = book_containers[i].find('a', class_='bookTitle')['href']
#     book_url = base_url + book_href
#     tmp = rating.get_text().split()
#     if len(tmp) > 6:    # special case of 'really liked it' in span
#       tmp = tmp[3:]
#     avg_rating = float(tmp[0])      # convert string to float
#     total_rating = int(tmp[4].replace(',',''))      # convert string to float
    
#     # Opening URLs
#     try:
#         ratings = get_book(book_url)
#         # print(ratings)
#     except:
#         ratings = []

#     data.append({
#         'title': title.get_text().strip(),
#         'author': author.get_text().strip(),
#         'avg_rating': avg_rating,
#         'total_rating': total_rating,
#         'ratings': ratings
#     })

# # Saving to dataset
# with open('goodreads.csv', 'w', encoding='UTF8') as f:
#     fields = ['title', 'author', 'avg_rating', 'total_rating', 'ratings']
#     writer = csv.DictWriter(f, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)