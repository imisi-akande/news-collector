# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['saharareporters.com']
    start_urls = ['http://saharareporters.com/news']

    def parse(self, response):
        pass
