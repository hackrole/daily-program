# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http.request import Request
from scrapy.utils import url
from scrapy.selector import Selector

from dmbt.items import CCUrlItem


class Cx11Spider(CrawlSpider):
    name = 'cx11'
    allowed_domains = ['1119cc.com']
    start_urls = [
        'http://www.119cc.com/htm/movielist6/1.htm',
        'http://www.119cc.com/htm/movielist6/2.htm',
        'http://www.119cc.com/htm/movielist6/3.htm',
        'http://www.119cc.com/htm/movielist6/4.htm',
        'http://www.119cc.com/htm/movielist6/5.htm',
        'http://www.119cc.com/htm/movielist6/6.htm',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'htm/movie6'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//dd[@class="film_title"]/@text()')
        imgs = response.xpath('//div[@class="box"]//img/@src')
        urls = response.xpath('//div[@id="urljiji"]//a/@href')

        title = ''.joiN(title.extract())
        imgs = imgs.extract()
        urls = ''.join(urls.extract())

        nurl = url.urljoin_rfc(response.request.url, url)
        yield Request(
            nurl, callback=self.parse_url,
            meta={
                'imgs': imgs,
                'title': title,
                'url': url,
            })

    def parse_url(self, response):
        hxs = Selector(response)
        download_url = hxs.re('jjvod_url = \'(.+)\';')

        meta = response.request.meta
        imgs = meta.get('imgs')
        title = meta.get('title')
        url = meta.get('url')

        item = CCUrlItem()
        item['url'] = url
        item['download_url'] = download_url
        item['title'] = title
        item['image_urls'] = imgs
        yield item
