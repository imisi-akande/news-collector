# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
import logging
logger = logging.getLogger('subjectslogger')

class NewsSpider(Spider):
    name = 'news'
    allowed_domains = ['saharareporters.com']
    start_urls = ['http://saharareporters.com']

    def __init__(self, story=None):
        self.story = story

    def parse(self, response):
        # scrape by stories by category or scrape all stories except for video stories
        if self.story:
            story_url = response.xpath('//li[contains(@class, "menu-mlid")]/a[contains(@href, "'+ self.story +'")]/@href').extract_first()
            if story_url != "/videos":
                absolute_story_url = response.urljoin(story_url)
                yield Request(absolute_story_url, callback = self.parse_stories)
        else:
            logger.info('Scraping all stories......... %s', response.url)
            stories = response.xpath('//li[contains(@class, "menu-mlid")]/a/@href').extract()
            for story in stories:
                if story != "/videos":
                    absolute_story_url = response.urljoin(story)
                    yield Request(absolute_story_url, callback=self.parse_stories)


    def parse_stories(self, response):
        ## scrape story attributes
        stories = response.xpath('//*[@class="block-module-content"]')
        for story in stories:
            category = story.xpath('.//a[@class="block-module-content-header-heading"]/text()').extract_first()
            headline = story.xpath('.//span[@class="block-module-content-header-title"]/a/text()').extract_first()
            release_date = story.xpath('.//div[contains(@class, "block-module-content-footer-item-date")]/text()').extract_first()

            yield{"category": category,
                  "headline": headline,
                  "release_date": release_date}

        next_page_url = response.xpath('//*[contains(@class, "pager-next")]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)
