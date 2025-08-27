# 代码生成时间: 2025-08-28 05:57:51
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from datetime import datetime, timedelta

# 定义一个定时任务调度器类
class ScheduledCrawler:
    def __init__(self, spider_name, interval):
        """
        定时任务调度器初始化
        :param spider_name: 爬虫名称
        :param interval: 定时执行的时间间隔（秒）
        """
        self.spider_name = spider_name
        self.interval = interval
        self.process = CrawlerProcess(get_project_settings())

    def start(self):
        """
        启动定时任务调度器
        """
        self._run_spider()
        reactor.addSystemEventTrigger('after', 'shutdown', self._stop)

    def _run_spider(self):
        """
        运行爬虫
        """
        try:
            # 启动爬虫
            self.process.crawl(self.spider_name)
        except Exception as e:
            # 错误处理
            print(f"Error running spider {self.spider_name}: {e}")
        finally:
            # 定时执行
            reactor.callLater(self.interval, self._run_spider)

    def _stop(self):
        """
        停止定时任务调度器
        """
        # 关闭爬虫进程
        self.process.stop()
        reactor.stop()

# 定义一个示例爬虫
class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://www.example.com']

    def parse(self, response):
        # 爬取数据
        print(response.url)

if __name__ == '__main__':
    # 设置定时任务调度器
    interval = 60 * 60  # 每小时执行一次
    scheduler = ScheduledCrawler('example', interval)
    scheduler.start()
    reactor.run()