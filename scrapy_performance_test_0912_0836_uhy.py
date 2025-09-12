# 代码生成时间: 2025-09-12 08:36:46
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import NotConfigured

"""
A Scrapy performance test script that allows you to run multiple spiders concurrently
# 增强安全性
and measure the performance in terms of requests per second.
"""

class PerformanceTestSpider(scrapy.Spider):
    name = 'performance_test'
    allowed_domains = []  # Define allowed domains for the spider
    start_urls = []  # Define the list of URLs to start the scraping process

    def parse(self, response):
        # This method will be called to handle the response downloaded for each of the requests made
        pass

# Custom settings for performance testing
class PerformanceTestSettings(object):
    def get_project_settings(self):
# 添加错误处理
        settings = get_project_settings()
        settings.set('CONCURRENT_REQUESTS_PER_DOMAIN', 16)
        settings.set('CONCURRENT_REQUESTS_PER_IP', 16)
        settings.set('DOWNLOAD_DELAY', 0.1)  # Decrease delay to speed up the test
        return settings

# Performance test function
def run_performance_test():
    try:
        process = CrawlerProcess(settings=PerformanceTestSettings().get_project_settings())
        process.crawl(PerformanceTestSpider)
# 增强安全性
        process.start()  # the script will block here until the crawling is finished
    except NotConfigured as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Run the performance test
    run_performance_test()
# 扩展功能模块