# -*- coding: utf-8 -*-

# Scrapy settings for cldm project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os

BOT_NAME = 'cldm'

SPIDER_MODULES = ['cldm.spiders']
NEWSPIDER_MODULE = 'cldm.spiders'

# Crawl responsibly by identifying yourself
# (and your website) on the user-agent
USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')

# speed
DOWNLOAD_DELAY = 0.25
CONCURRENT_REQUESTS_PER_IP = 2

# httpcache
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'caches')

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': None,
}

# cookies
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# download image
IMAGES_STORE = "/var/www/cl_images/"
ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
}

# retry
DOWNLOAD_TIMEOUT = 60
RETRY_ENABLED = True
