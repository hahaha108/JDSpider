# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    content= scrapy.Field()
    url = scrapy.Field()

class JdcommentItem(scrapy.Item):

    content = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()