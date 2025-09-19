# 代码生成时间: 2025-09-19 21:30:12
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from datetime import datetime, timedelta
import schedule

"""
定时任务调度器，用于定时运行Scrapy爬虫
"""

class SpiderScheduler:
    def __init__(self, spider_name, interval):
        """
        初始化调度器
        :param spider_name: 爬虫名称
        :param interval: 定时间隔（秒）
        """
        self.spider_name = spider_name
        self.interval = interval
        self.process = None

    def run_spider(self):
        """
        运行Scrapy爬虫
        """
        try:
            self.process = CrawlerProcess(get_project_settings())
            self.process.crawl(self.spider_name)
            self.process.start()
        except Exception as e:
            print(f"Error running spider {self.spider_name}: {e}")

    def schedule_spider(self):
        """
        定时运行爬虫
        """
        schedule.every(self.interval).seconds.do(self.run_spider)

    def start(self):
        """
        启动调度器
        """
        self.schedule_spider()
        while True:
            schedule.run_pending()
            reactor.sleep(1)

# 使用示例
if __name__ == "__main__":
    configure_logging({'LOG_LEVEL': 'INFO'})
    scheduler = SpiderScheduler('MySpider', 60*60)  # 每小时运行一次
    scheduler.start()