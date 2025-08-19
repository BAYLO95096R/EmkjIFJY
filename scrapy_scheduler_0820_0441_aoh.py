# 代码生成时间: 2025-08-20 04:41:27
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

# 定义定时任务调度器类
class Scheduler:
    def __init__(self, spider_class):
        self.spider_class = spider_class
        self.process = None

    def start(self):
        """启动定时任务调度器"""
        try:
            # 创建CrawlerProcess实例
            self.process = CrawlerProcess(get_project_settings())
            # 创建BackgroundScheduler实例
            scheduler = BackgroundScheduler()
            scheduler.start()

            # 定义定时任务触发器
            trigger = CronTrigger(hour=10, minute=30)  # 每天10:30执行

            # 添加定时任务
            scheduler.add_job(self.run_spider, trigger)

            # 启动调度器
            print("定时任务调度器启动成功...")

        except Exception as e:
            print(f"启动定时任务调度器失败: {e}")

    def stop(self):
        """停止定时任务调度器"""
        if self.process:
            self.process.stop()
            print("定时任务调度器停止成功...")

    def run_spider(self):
        """运行Scrapy Spider"""
        try:
            # 运行Scrapy Spider
            self.process.crawl(self.spider_class)
            self.process.start()
            print(f"{self.spider_class.__name__} 运行成功...")
        except Exception as e:
            print(f"运行{self.spider_class.__name__} 失败: {e}")

# 示例用法
if __name__ == "__main__":
    # 定义Scrapy Spider类
    class MySpider(scrapy.Spider):
        name = "my_spider"
        start_urls = ["http://example.com"]

        def parse(self, response):
            print("解析网页...")
            return {}

    # 创建调度器实例
    scheduler = Scheduler(MySpider)

    # 启动调度器
    scheduler.start()

    # 等待调度器运行
    try:
        while True:
            pass
    except KeyboardInterrupt:
        scheduler.stop()
