# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class articles(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    body = scrapy.Field()
    link = scrapy.Field()
    
class article(scrapy.Item):
    paragraph = scrapy.Field()
    title = scrapy.Field()
    
