from scrapy import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from indeed.items import IndeedItem

class IndeedSpider(Spider):
    name = "indeed"
    allowed_domains = ["indeed.com"]
    start_urls = [
        "https://www.indeed.com/jobs?q=software+engineer",
    ]

    def parse(self, response):
      jobs = Selector(response).xpath('//div[@id="mosaic-zone-jobcards"]//li//td[@class="resultContent"]')

      for job in jobs:
        item = IndeedItem()
        item['title'] = job.xpath('//a[@class="jcs-JobTitle css-jspxzf eu4oa1w0"]//text()').get()
        item['url'] = job.xpath('//a[@class="jcs-JobTitle css-jspxzf eu4oa1w0"]//@href').get()
        print(item['title'])
        print()
        yield item

        # jcs-JobTitle css-jspxzf eu4oa1w0