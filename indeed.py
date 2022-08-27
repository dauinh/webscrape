from unittest import result
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

headers = {
  # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
  "Accept-Encoding": "gzip, deflate, br",
  "accept-language": "en-GB",
  "server": "cloudflare",
  "accept" :"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
  "Dnt": "1",
  "Host": "httpbin.org",
  "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
  }
URL = "https://indeed.com/jobs?q=software+engineer"
# URL = "https://www.indeed.com/q-software-engineer-jobs.html"
r = requests.get(URL, headers=headers)
print(r.status_code)
# soup=BeautifulSoup(r.text,"html.parser")

# req = Request(URL)
# page = urlopen(req).read()
# page = requests.get(URL)


# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="mosaic-zone-jobcards")
# job_elements = results.find_all("li")
# print(results)
