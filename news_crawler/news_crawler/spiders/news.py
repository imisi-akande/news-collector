# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class NewsSpider(Spider):
    name = 'news'
    allowed_domains = ['saharareporters.com']
    start_urls = ['http://saharareporters.com/news']

    def parse(self, response):
        stories = response.xpath('//*[@class="block-module-content"]')
        for story in stories:
            category = story.xpath('.//a[@class="block-module-content-header-heading"]/text()').extract_first()
            headline = story.xpath('.//span[@class="block-module-content-header-title"]/a/text()').extract_first()
            comments = story.xpath('.//a[@data-disqus-identifier="node/78199"]/text()').extract_first()
            release_date = story.xpath('.//div[contains(@class, "block-module-content-footer-item-date")]/text()').extract_first()

            yield{"category": category,
                  "headline": headline,
                  "release_date": release_date}

        next_page_url = response.xpath('//*[contains(@class, "pager-next")]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)
