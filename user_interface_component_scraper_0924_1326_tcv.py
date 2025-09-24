# 代码生成时间: 2025-09-24 13:26:28
User Interface Component Scraper

This Scrapy Spider is designed to scrape user interface components from a website.

It is structured to be modular, easy to understand, and maintainable.

"""

import scrapy

from scrapy.crawler import CrawlerProcess

from scrapy.exceptions import CloseSpider

from scrapy.loader import ItemLoader

from scrapy.item import Field, Item

from scrapy.spiders import Spider

from scrapy.selector import Selector

from scrapy.http import Request

import logging


# Define the item that will be used to store scraped data
class ComponentItem(Item):
    name = Field()
    description = Field()
    url = Field()
    screenshot_url = Field()

# Define the Spider
class ComponentSpider(Spider):
    name = 'component_spider'
    allowed_domains = ['example.com']  # Replace with the actual domain
    start_urls = [
        "https://example.com/components",
    ]

    def parse(self, response):
        """Parse the start URL and extract component URLs."""
        # Navigate to the list of components
        component_selector = 'div.component-list'
        for component in response.css(component_selector):
            # Extract the URL of each component
            url = component.css('a::attr(href)').get()
            yield response.follow(url, callback=self.parse_component)

    def parse_component(self, response):
        """Parse a single component page and extract details."""
        # Load the item
        item_loader = ItemLoader(item=ComponentItem(), selector=response)
        item_loader.add_css('name', 'h1.component-name::text')
        item_loader.add_css('description', 'div.component-description::text')
        item_loader.add_value('url', response.url)
        item_loader.add_css('screenshot_url', 'img.screenshot::attr(src)')

        # Load the item and yield it
        yield item_loader.load_item()

# Function to run the spider
def run_spider():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'LOG_LEVEL': logging.INFO,
    })
    process.crawl(ComponentSpider)
    process.start()

if __name__ == '__main__':
    run_spider()
