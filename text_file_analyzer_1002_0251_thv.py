# 代码生成时间: 2025-10-02 02:51:22
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider, Request
from scrapy.exceptions import CloseSpider
from collections import Counter
import logging


# 设置日志记录器
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextFileAnalyzerSpider(Spider):
    name = 'text_file_analyzer'
    allowed_domains = []
    start_urls = []
    # 需要分析的文件路径
    file_path = ''

    def __init__(self, file_path='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = file_path

    def parse(self, response):
        """
        解析文本文件内容并进行分析
        :param response: 包含文件内容的响应对象
        :return: 无
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # 分析文本内容
                self.analyze_text(content)
        except FileNotFoundError:
            logger.error(f'文件 {self.file_path} 未找到。')
            raise CloseSpider(reason='File not found')
        except Exception as e:
            logger.error(f'解析文件时发生错误：{e}')
            raise CloseSpider(reason='Error parsing file')

    def analyze_text(self, text):
        """
        分析文本内容
        :param text: 文件内容
        :return: 无
        """
        # 将文本分割为单词列表
        words = text.split()
        # 统计每个单词的出现次数
        word_counts = Counter(words)
        # 打印最常见的10个单词及其出现次数
        most_common_words = word_counts.most_common(10)
        logger.info('最常见的10个单词及其出现次数：')
        for word, count in most_common_words:
            logger.info(f'{word}: {count}')


# 创建Scrapy处理器
process = CrawlerProcess()

# 添加爬虫并设置文件路径参数
process.crawl(TextFileAnalyzerSpider, file_path='path_to_your_text_file.txt')

# 启动爬虫
process.start()