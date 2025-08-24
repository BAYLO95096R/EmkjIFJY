# 代码生成时间: 2025-08-24 13:25:11
import psutil
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider, Request
from scrapy.exceptions import NotConfigured


# 设置日志记录
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class MemoryUsageSpider(Spider):
    name = "memory_usage_spider"
    allowed_domains = []
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(MemoryUsageSpider, self).__init__(*args, **kwargs)
        # 检查是否安装了psutil库
        try:
            import psutil
        except ImportError:
            raise NotConfigured("Missing required library 'psutil', install it with 'pip install psutil'.")

    def start_requests(self):
        # 发送请求以启动爬虫
        yield Request(url="http://example.com", callback=self.parse)

    def parse(self, response):
        # 获取内存使用情况
        try:
            # 获取进程的内存使用情况
            process_memory = psutil.Process().memory_info().rss
            logger.info(f"Process memory usage: {process_memory} bytes")

            # 获取系统内存使用情况
            system_memory = psutil.virtual_memory()
            logger.info(f"Total system memory: {system_memory.total} bytes")
            logger.info(f"Available system memory: {system_memory.available} bytes")
            logger.info(f"Used system memory: {system_memory.used} bytes")
            logger.info(f"System memory usage percentage: {system_memory.percent}%")

            # 可以在这里添加更多的内存使用情况分析代码

        except Exception as e:
            logger.error(f"Error occurred while getting memory usage: {e}")


# 设置CrawlerProcess以运行爬虫
process = CrawlerProcess()
process.crawl(MemoryUsageSpider)
process.start()
