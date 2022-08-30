# TODO:
#   Write automation for scraping books
#   Save to dataset (xls/csv)

import requests
from bs4 import BeautifulSoup as bs
import csv
import time
import subprocess as sp

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.quit()

test_driver_manager_chrome()

# Scraping
# url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
# page = requests.get(url)
# soup = bs(page.content, 'html.parser')
# book_containers = soup.find_all('tr')

# Testing open URLs
# base_url = 'https://www.goodreads.com'
# book = book_containers[0]
# book_href = book.find('a', class_='bookTitle')['href']
# book_url = base_url + book_href
# command = ['python3', '-m', 'webbrowser', book_url]
# process = sp.Popen(command, stdout=sp.PIPE)
# output, error = process.communicate()


# data = []
# for i in range(len(book_containers)):
#     title = book_containers[i].find('a', class_='bookTitle')
#     author = book_containers[i].find('a', class_='authorName')
#     rating = book_containers[i].find('span', class_='minirating')
#     tmp = rating.get_text().split()
#     data.append({
#         'title': title.get_text().strip(),
#         'author': author.get_text().strip(),
#         'avg_rating': tmp[0],
#         'total_rating': tmp[4]
#     })

# # Saving to dataset
# with open('goodreads.csv', 'w', encoding='UTF8') as f:
#     fields = ['title', 'author', 'avg_rating', 'total_rating']
#     writer = csv.DictWriter(f, fieldnames=fields)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)