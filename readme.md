# Webscrape

This project explores how to scrape the web.

## Scrapy

Use the framework [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html) to extract data from [stackoverflow.com](https://stackoverflow.com/questions?pagesize=50&sort=newest) and [indeed.com](https://www.indeed.com/q-software-engineer-jobs.html). However, indeed.com does not allow for bots, so there is no data gathered from this website. 

> **_NOTE:_**  To see which bots are allowed, check for a website robot.txt file.

## BeautifulSoup & Selenium

Use the package [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Selenium](https://www.selenium.dev/documentation/overview/) to extract data from [goodreads.com](https://www.goodreads.com/list/show/1.Best_Books_Ever).

Gather data about: book title, author, average ratings, total ratings, top genres, (description), rating histograms

### TODO
- [ ] Write automation for scraping books
- [ ] Save to dataset (xls/csv)