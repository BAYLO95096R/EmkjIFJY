# 代码生成时间: 2025-09-23 17:36:45
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import NotConfigured
import psutil
import platform
import time

# 内存使用情况分析Spider
class MemoryUsageSpider(scrapy.Spider):
    name = 'memory_usage'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (compatible; MemoryUsageSpider +http://yourdomain.com)",
        "FEEDS": {
            'memory_usage.json': {
                'format': 'json',
                'store_empty': False,
            }
        }
    }

    def __init__(self, *args, **kwargs):
        super(MemoryUsageSpider, self).__init__(*args, **kwargs)
        if platform.system() == 'Windows':
            self.pid = psutil.Process().pid
        else:
            self.pid = self.getpid()  # 获取当前进程PID
        self.start_time = time.time()
        self.start_memory_usage = psutil.Process(self.pid).memory_info().rss

    def get_memory_usage(self):
        """获取当前进程的内存使用情况"""
        try:
            process = psutil.Process(self.pid)
            return process.memory_info().rss
        except Exception as e:
            self.logger.error(f"获取内存使用情况失败: {e}")
            raise NotConfigured(f"无法获取内存使用情况: {e}")

    def start_requests(self):
        """启动请求并获取内存使用情况"""
        self.logger.info("开始分析内存使用情况...")
        memory_usage = self.get_memory_usage()
        yield scrapy.Request(
            url="http://example.com",
            callback=self.parse,
            meta={'memory_usage': memory_usage}
        )

    def parse(self, response):
        """解析响应并记录内存使用情况"""
        memory_usage = response.meta['memory_usage']
        end_time = time.time()
        duration = end_time - self.start_time
        self.logger.info(f"结束分析内存使用情况. 总耗时: {duration}秒. 使用内存: {memory_usage}字节")
        self.crawler.stats.set_value('memory_usage', memory_usage)
        yield {'memory_usage': memory_usage, 'duration': duration}

# 运行Spider
if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(MemoryUsageSpider)
    process.start()
