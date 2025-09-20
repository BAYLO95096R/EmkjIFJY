# 代码生成时间: 2025-09-20 13:11:08
# -*- coding: utf-8 -*-

"""
This is a Scrapy spider for scraping user interface components.
It is designed to be clear, maintainable, and extensible.
"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.exceptions import NotConfigured


# Define the item structure for UI components
class UIComponent(Item):
    name = Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst())
    description = Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst())
    source_url = Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst())
    preview_image_url = Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst())


# Define a spider that will scrape UI components
class UIComponentSpider(Spider):
    name = 'ui_component_spider'
    allowed_domains = []  # Define the target domain
    start_urls = []  # Define the start URLs

    def __init__(self, *args, **kwargs):
        super(UIComponentSpider, self).__init__(*args, **kwargs)
        # Check if the spider is configured properly
        if not self.allowed_domains or not self.start_urls:
            raise NotConfigured("Please define allowed_domains and start_urls")

    def parse(self, response):
        # Extract UI components from the response
        for component in response.css('div.component'):
            loader = ItemLoader(item=UIComponent(), selector=response)
            loader.add_css('name', 'h1.component-name::text')
            loader.add_css('description', 'p.component-description::text')
            loader.add_value('source_url', response.url)
            loader.add_css('preview_image_url', 'img.component-preview::attr(src)')
            yield loader.load_item()

        # Follow pagination links if available
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        # Handle spider closure
        if reason == 'finished':
            print('Spider finished successfully.')
        else:
            print(f'Spider closed due to {reason}')


# Set up the process to run the spider
def run_spider():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (compatible; UIComponentSpider/1.0)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'ui_components.json',
    })
    process.crawl(UIComponentSpider)
    process.start()


if __name__ == '__main__':
    run_spider()