# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils import url

from dmbt.items import UrlItem


class BtshareSpider(CrawlSpider):
    name = 'btshare'
    allowed_domains = ['btshare.net']
    start_urls = [
        'http://www.btshare.net/sort-6-1.html',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'sort-6-(.+?).html'), follow=True),
        Rule(LinkExtractor(allow=r'show-(.+).html'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        intro = response.xpath('//div[@class="intro"]').extract()
        imgs = response.xpath('//div[@class="intro"]//img/@src').extract()

        bt_url = ''.join(response.xpath('//a[@id="download"]/@href').extract())
        bt_url = url.urljoin_rfc(response.request.url, bt_url)

        item = UrlItem()
        item['url'] = response.request.url
        item['bt_url'] = bt_url
        item['title'] = intro
        item['image_urls'] = imgs

        yield item
