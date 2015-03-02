# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from cldm.items import CldmItem


class DmSpider(CrawlSpider):
    name = 'dm'
    allowed_domains = [
        'cl.yyq.im',
        'rmdown.com',
    ]
    start_urls = [
        'http://cl.yyq.im/thread0806.php?fid=5&page=%s&search=' % i
        for i in range(1, 67)
    ]

    rules = (
        Rule(LinkExtractor(allow=r'htm_data/5/\d+/\d+.html'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = CldmItem()
        item['title'] = response.xpath('//h4/text()').extract()
        item['desc'] = response.xpath(
            '//div[@class="tpc_content"][1]//text()').extract()
        item['image_urls'] = response.xpath(
            '//div[@class="tpc_content"][1]//img/@src').extract()
        item['url'] = response.xpath(
            '//div[@class="tpc_content"][1]//a/text()').extract()

        yield item
