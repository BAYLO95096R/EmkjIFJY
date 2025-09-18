# 代码生成时间: 2025-09-19 01:38:30
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings
from scrapy.commands import ScrapyCommand
from scrapy.utils.conf import build_component_list
from scrapy import signals
import logging

# 数据分析器中间件，用于统计分析爬取数据
class DataAnalysisMiddleware:
    def __init__(self):
        self.stats = {}

    def process_spider_output(self, response, result, spider):
        # 统计每个spider返回的数据条目数
        if response.meta.get('dont_merge'):
            return result
        for res in result:
            self.stats.setdefault(res['_type'], []).append(res)
        return result

    def get_stats(self):
        return self.stats

# 数据分析器命令，用于启动Scrapy爬虫并输出统计分析结果
class DataAnalysisCommand(ScrapyCommand):
    requires_project = False
    default_settings = {}

    def short_desc(self):
        return 'Run a command with the Scrapy framework'

    def run(self, args, opts):
        try:
            # 构建Scrapy命令行组件列表
            commands = build_component_list(ScrapyCommand, settings)
            # 创建Scrapy命令行处理器
            process = CrawlerProcess(get_project_settings())
            # 添加数据分析器中间件
            process.crawl(DataAnalysisMiddleware)
            process.start(args)
            # 获取统计分析结果
            stats = process.crawled_once
            if stats:
                self.print_stats(stats.get_stats())
            else:
                logging.error('No stats to display')
        except NotConfigured as e:
            logging.error(e)

    def print_stats(self, stats):
        logging.info('Data analysis stats:')
        for key, value in stats.items():
            logging.info(f'{key}: {len(value)}')

# 设置Scrapy项目
settings = get_project_settings()

if __name__ == '__main__':
    # 注册数据统计分析命令
    DataAnalysisCommand.run(['scrapy', 'data-analysis'], {})