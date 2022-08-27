import requests
from bs4 import BeautifulSoup as bs
import csv
# NOTES:
# Open urls in terminal
#   python3 -m webbrowser https://stackoverflow.com

# Todo:
#   Write automation for scraping books
#   Save to dataset (xls/csv)

# Scraping
# url = "https://www.goodreads.com/choiceawards/best-books-2021?ref=nav_brws_gca"
url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
page = requests.get(url)
soup = bs(page.content, 'html.parser')
# print(soup)
# titles = soup.find_all('a', class_='bookTitle')
# authors = soup.find_all('a', class_='authorName')
# average_ratings = soup.find_all('a', class_='minirating')
book_containers = soup.find_all('tr')
# print(type(book_containers))
# print(len(book_containers))
data = []
for i in range(len(book_containers)):
    title = book_containers[i].find('a', class_='bookTitle')
    author = book_containers[i].find('a', class_='authorName')
    rating = book_containers[i].find('span', class_='minirating')
    tmp = rating.get_text().split()
    data.append({
        'title': title.get_text().strip(),
        'author': author.get_text().strip(),
        'avg_rating': tmp[0],
        'total_rating': tmp[4]
    })

# Saving to dataset
with open('goodreads.csv', 'w', encoding='UTF8') as f:
    fields = ['title', 'author', 'avg_rating', 'total_rating']
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)