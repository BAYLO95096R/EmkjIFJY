# 代码生成时间: 2025-08-20 15:05:22
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
from urllib.parse import urlparse
import requests

# 定义一个用来验证URL有效性的Spider
class URLValidatorSpider(scrapy.Spider):
    name = "url_validator"
    allowed_domains = []
    start_urls = []

    def __init__(self, start_urls=None, *args, **kwargs):
        # 从命令行参数或项目配置中获取起始URLs
        if not start_urls:
            raise NotConfigured("需要提供起始URL列表")
        self.start_urls = start_urls

    def parse(self, response):
        # 解析响应，验证URL有效性
        yield {
            'url': response.url,
            'is_valid': True
        }

    def check_url(self, url):
        # 检查URL是否有效
        try:
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                # 对有效的URL执行HTTP请求
                response = requests.head(url, timeout=5)
                if response.status_code == 200:
                    return True
        except (requests.RequestException, ValueError):
            pass
        return False

# 设置处理器
process = CrawlerProcess()

# 定义要验证的URLs
urls_to_check = [
    "http://example.com",
    "https://nonexistentwebsite.org"
]

# 添加Spider到处理器并开始爬取
def crawl_urls(urls):
    process.crawl(URLValidatorSpider, start_urls=urls)
    process.start()

# 执行爬虫
if __name__ == '__main__':
    crawl_urls(urls_to_check)