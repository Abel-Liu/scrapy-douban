# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    rate = scrapy.Field()
    year = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()
    seen = scrapy.Field()
    creation_time = scrapy.Field()
    update_time = scrapy.Field()
