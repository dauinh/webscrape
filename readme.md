# Webscrape At a Glance

This project explores how to scrape the web.

## Scrapy

Use the framework [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html) to extract data from [stackoverflow.com](https://stackoverflow.com/questions?pagesize=50&sort=newest) and [indeed.com](https://www.indeed.com/q-software-engineer-jobs.html). However, indeed.com does not allow for bots, so there is no data gathered from this website. 

> **_NOTE:_**  To see which bots are allowed, check for a website robot.txt file.

## BeautifulSoup & Selenium

Use the package [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Selenium](https://www.selenium.dev/documentation/overview/) to extract data from [Goodreads' best books ever](https://www.goodreads.com/list/show/1.Best_Books_Ever) and save to a csv file.

Gather data about: book title, author, average ratings, total ratings, top genres, rating distribution

Top genres and rating distribution are gathered by accessing each book's website. However, both categories have missing values (about half). Goodreads has a function to determine how the webpage looks like based on how many signed out pagehits there are and how recent is the interstitial. Current script is based on Goodreads with React components.