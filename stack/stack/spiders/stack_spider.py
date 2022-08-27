from scrapy import Spider
from scrapy import Selector
from stack.items import StackItem

class StackSpider(Spider):
  name = "stack"
  allowed_domains = ["stackoverflow.com"]
  start_urls = [
    "https://stackoverflow.com/questions?pagesize=50&sort=newest"
  ]

  def parse(self, response):
    # "Unit testing"
    # filename = 'stackoverflow.html'
    # with open(filename, 'wb') as f:
    #   f.write(response.body)
    # self.log('Saved stackoverflow')

    questions = Selector(response).xpath('//div[@class="s-post-summary--content"]/h3')

    for question in questions:
      item = StackItem()
      item['title'] = question.xpath(
        'a[@class="s-link"]/text()').get()
      item['url'] = question.xpath(
        'a[@class="s-link"]/@href').get()
      yield item