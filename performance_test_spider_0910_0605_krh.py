# 代码生成时间: 2025-09-10 06:05:46
import scrapy
def create_project(project_name):
    # Create a Scrapy project
    from scrapy.cmdline import execute
    execute(['scrapy', 'startproject', project_name])

def create_spider(project_name, spider_name):
    # Create a Scrapy spider
    execute(['scrapy', 'genspider', spider_name, 'example.com'])
def setup_middlewares(project_name):
    # Set up middlewares for performance testing
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    from scrapy.exceptions import CloseSpider, NotConfigured
    class PerformanceMiddleware(object):
        # Custom middleware for performance testing
        def process_request(self, request, spider):
            # Record the request start time
            request.meta['start_time'] = time.time()
            return None
        
        def process_response(self, request, response, spider):
            # Record the response end time and calculate the response time
            elapsed = time.time() - request.meta.get('start_time', time.time())
            response.meta['download_latency'] = elapsed
            spider.crawler.stats.set_value('response_time', elapsed, spider=spider)
            return response
def performance_test(project_name, spider_name):
    # Configuration for performance testing
    class Settings(object):
        # Custom settings for performance testing
        CLOSESPIDER_TIMEOUT = 30
        CLOSESPIDER_ITEMCOUNT = 100
        # Add custom middlewares
        DOWNLOADER_MIDDLEWARES = {
            'myproject.middlewares.PerformanceMiddleware': 543,
        }
    # Create a CrawlerProcess instance with custom settings
    process = CrawlerProcess(settings=Settings())
    # Start the crawler
    process.crawl(spider)
    process.start()

def main():
    # Entry point of the script
    project_name = 'myproject'
    spider_name = 'myspider'
    create_project(project_name)
    create_spider(project_name, spider_name)
    setup_middlewares(project_name)
    performance_test(project_name, spider_name)
if __name__ == '__main__':
    main()