# -*- coding: utf-8 -*-

# Scrapy settings for dmbt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dmbt'

SPIDER_MODULES = ['dmbt.spiders']
NEWSPIDER_MODULE = 'dmbt.spiders'

ITEM_PIPELINES = [
    'scrapy.contrib.pipeline.images.ImagesPipeline',
]

IMAGES_STORE = "/home/daipeng/Desktop/imgs"

# Crawl responsibly by identifying yourself (and your website)
# on the user-agent
# USER_AGENT = 'dmbt (+http://www.yourdomain.com)'
