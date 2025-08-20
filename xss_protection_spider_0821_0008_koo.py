# 代码生成时间: 2025-08-21 00:08:51
import scrapy
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from scrapy.exceptions import NotConfigured

# 引入HTML转义函数
from html import escape

class XSSProtectionSpider(Spider):
    '''
    XSS Protection Spider
    This spider is designed to protect against XSS attacks by escaping HTML special characters.
    It can be used as a middleware or applied to specific items.
    '''
    name = 'xss_protection_spider'

    def __init__(self, *args, **kwargs):
        super(XSSProtectionSpider, self).__init__(*args, **kwargs)
        # 检查是否配置了允许的域，如果没有则抛出异常
        if not getattr(self, 'allowed_domains', None):
            raise NotConfigured('allowed_domains must be set for this spider')

    def start_requests(self):
        '''
        Start the scraping process by yielding Requests.
        '''
        urls = [
            'https://example.com/page1',
            'https://example.com/page2'
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        Parse the response and yield items.
        This method is called for each response downloaded.
        '''
        # 使用Selector解析响应内容
        sel = Selector(response)
        # 获取页面上的文本内容
        text = sel.css('::text').get()
        # 对文本内容进行HTML转义
        escaped_text = escape(text)
        
        # 装载数据到Item
        item_loader = ItemLoader(item={}, response=response)
        item_loader.add_value('escaped_text', escaped_text)
        
        # 生成item并返回
        yield item_loader.load_item()

    def process_item(self, item, spider):
        '''
        Process each item before it is yielded to the pipeline.
        This method is useful for cleaning, normalizing, and
        transforming data before it is yielded to the pipeline.
        '''
        # 这里可以添加更多的处理逻辑
        # 例如，进一步清理或验证数据
        
        return item