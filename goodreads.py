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

chromedriver_autoinstaller.install()

def test_chromedriver():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    title = driver.title
    print(title)
    driver.implicitly_wait(3)

def get_book(url):
    # driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    # print(title)
    driver.implicitly_wait(7)
    get_rating = driver.find_elements(By.CSS_SELECTOR, '[aria-label="Number of ratings and percentage of total ratings"]')
    get_genre = driver.find_elements(By.CLASS_NAME, 'BookPageMetadataSection__genre')

    genres = []
    for i in range(len(get_genre)):
        tag = get_genre[i].get_attribute('innerText')
        genres.append(tag)

    ratings = []
    for i in range(len(get_rating)):
        text = get_rating[i].text
        text = int(text.split()[0].replace(',',''))
        ratings.append(text)

    driver.close()

    return genres, ratings


# Scraping
url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
base_url = 'https://www.goodreads.com'
page = requests.get(url)
soup = bs(page.content, 'html.parser')
book_containers = soup.find_all('tr')

data = []
for i in range(len(book_containers)):
    title = book_containers[i].find('a', class_='bookTitle')
    author = book_containers[i].find('a', class_='authorName')
    rating = book_containers[i].find('span', class_='minirating')
    book_href = book_containers[i].find('a', class_='bookTitle')['href']
    book_url = base_url + book_href
    tmp = rating.get_text().split()
    if len(tmp) > 6:    # special case of 'really liked it' in span
      tmp = tmp[3:]
    avg_rating = float(tmp[0])      # convert string to float
    total_rating = int(tmp[4].replace(',',''))      # convert string to float
    
    # Opening URLs
    try:
        genres, ratings = get_book(book_url)
        # print(genres)
        # print(ratings)
    except:
        genres = []
        ratings = []

    data.append({
        'title': title.get_text().strip(),
        'author': author.get_text().strip(),
        'avg_rating': avg_rating,
        'total_rating': total_rating,
        'top_genres': genres,
        'rating_distribution': ratings
    })

# Saving to dataset
with open('goodreads.csv', 'w', encoding='UTF8') as f:
    fields = ['title', 'author', 'avg_rating', 'total_rating', 'top_genres', 'rating_distribution']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)