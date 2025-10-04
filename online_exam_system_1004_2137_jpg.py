# 代码生成时间: 2025-10-04 21:37:43
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider, Request
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from scrapy.item import Field, Item
from scrapy.utils.response import open_in_browser
from scrapy.http import HtmlResponse
from twisted.internet.error import DNSLookupError, TimeoutError, TCP4ConnectionError
import logging

# 设置日志记录级别
logging.basicConfig(level=logging.INFO)

# 定义Item结构
class ExamItem(Item):
    title = Field()
    question = Field()
    options = Field()
    answer = Field()

# 定义Spider
class ExamSpider(Spider):
    name = 'exam_spider'
    allowed_domains = ['example.com']  # 这里替换为在线考试系统的实际域名
    start_urls = [
        'http://example.com/exam',  # 这里替换为在线考试系统的实际URL
    ]

    def parse(self, response: HtmlResponse):
        # 解析页面
        exam_loader = ItemLoader(item=ExamItem(), selector=response)
        exam_loader.add_xpath('title', '//title/text()'),
        exam_loader.add_xpath('question', '//h1/text()'),
        exam_loader.add_xpath('options', '//ul/li/text()'),
        exam_loader.add_xpath('answer', '//h2/text()')
        yield exam_loader.load_item()

        # 跟随下一页链接
        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        # 关闭时的处理
        logging.info(f'Spider closed: {reason}')

# 主函数，用于运行Spider
def main():
    try:
        process = CrawlerProcess(settings={'USER_AGENT': 'Mozilla/5.0'})
        process.crawl(ExamSpider)
        process.start()
    except DNSLookupError:
        logging.error('DNS lookup error occurred')
    except TimeoutError:
        logging.error('Timeout error occurred')
    except TCP4ConnectionError:
        logging.error('TCP connection error occurred')
    except CloseSpider:
        logging.error('Spider was closed')
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()