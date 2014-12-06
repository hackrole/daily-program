# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmbtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UrlItem(scrapy.Item):
    url = scrapy.Field()
    bt_url = scrapy.Field()
    title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class CCUrlItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    download_url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
