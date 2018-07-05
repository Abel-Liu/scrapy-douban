# -*- coding: utf-8 -*-
import scrapy
from doubanspider.items import *
import json
from datetime import datetime


class doubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0"]

    def parse(self, response):
        data = json.loads(response.text)
        for i in data.get("data"):
            item = DoubanspiderItem()
            item["id"] = i.get("id")
            item["name"] = i.get("title")
            item["url"] = i.get("url")
            item["rate"] = i.get("rate")
            item["cover"] = i.get("cover")
            item["creation_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item["update_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item["seen"] = 0

            yield scrapy.Request(item["url"], meta={"item": item}, callback=self.parse_detail)

        if data.get("data") and len(data.get("data")) > 0:
            start = int(response.url[response.url.rfind("start=") + 6:]) + 20
            next_page = response.url[:response.url.rfind("start=") + 6] + str(start)
            yield scrapy.Request(next_page)

    def parse_detail(self, response):
        item = response.meta["item"]
        item["year"] = response.xpath("//div[@id='content']/h1/span[@class='year']/text()").extract_first()
        item["year"] = item["year"].replace("(", "").replace(")", "")
        item["description"] = response.xpath(
            "//div[@id='link-report']/span[contains(@class,'all')]/text()").extract_first()
        item["category"] = ','.join(response.xpath("//div[@id='info']/span[@property='v:genre']/text()").extract())
        yield item
