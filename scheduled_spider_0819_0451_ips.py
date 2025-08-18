# 代码生成时间: 2025-08-19 04:51:35
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from apscheduler.schedulers.twisted import TwistedScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from scrapy.exceptions import NotConfigured


# 定义定时任务调度器
class ScheduledSpider:
    def __init__(self, spider_name, schedule_interval):
        self.spider_name = spider_name
        self.schedule_interval = schedule_interval
        self.scheduler = TwistedScheduler(
            jobstores={"default": MemoryJobStore()},
            job_defaults={"coalesce": False, "max_instances": 1},
        )

    def start_job(self, jobstore=None, executor=None):
        if jobstore:
            self.scheduler.configure(
                jobstores={"default": jobstore}
            )
        if executor:
            self.scheduler.configure(
                executors={"default": executor}
            )
        self.add_job(self.run_spider, trigger="cron", hour=self.schedule_interval)
        self.scheduler.start()

    def run_spider(self):
        # 获取Scrapy项目设置
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        try:
            # 启动爬虫
            process.crawl(self.spider_name)
            process.start()
        except Exception as e:
            print(f"Error running spider: {e}")

    def add_job(self, job_func, trigger, **trigger_args):
        # 添加定时任务
        self.scheduler.add_job(job_func, trigger, **trigger_args)


# 定时任务调度器配置
def main():
    spider_name = "YourSpider"  # 替换为你的爬虫名称
    schedule_interval = "0 12 * * *"  # 每天中午12点执行
    jobstore = SQLAlchemyJobStore(url="sqlite:///apscheduler.db")
    executor = ProcessPoolExecutor(max_workers=2)

    scheduler = ScheduledSpider(spider_name, schedule_interval)
    scheduler.start_job(jobstore=jobstore, executor=executor)

    reactor.run()  # 启动Twisted事件循环


if __name__ == "__main__":
    main()