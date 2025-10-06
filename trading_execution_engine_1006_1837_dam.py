# 代码生成时间: 2025-10-06 18:37:46
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import CloseSpider

# Define the trading engine class
class TradingEngine:
    def __init__(self, settings):
        self.settings = settings
        self.process = CrawlerProcess(settings)

    def start_spider(self, spider_name):
        """Start a spider by its name."""
        try:
            self.process.crawl(spider_name)
            self.process.start()
        except CloseSpider:
            print(f"Spider {spider_name} closed unexpectedly.")
        except Exception as e:
            print(f"An error occurred while starting spider {spider_name}: {e}")

    def add_spider(self, spider):
        """Add a new spider to the engine."""
        self.process.crawlers[0].spiders.load(spider)

    def stop(self):
        """Stop the engine and all running spiders."""
        self.process.stop()

# Define a simple spider as an example
class SimpleSpider(scrapy.Spider):
    name = 'simple_spider'
    start_urls = ['http://example.com']

    def parse(self, response):
        """Parse the response and yield results."""
        # This is a placeholder for actual parsing logic
        yield {
            'title': response.xpath('//title/text()').get(),
            'body': response.xpath('//body//p/text()').getall()
        }

# Example usage
if __name__ == '__main__':
    settings = get_project_settings()
    engine = TradingEngine(settings)

    # Add your spiders to the engine
    engine.add_spider(SimpleSpider)

    # Start the engine and run the spider
    engine.start_spider(SimpleSpider.name)
