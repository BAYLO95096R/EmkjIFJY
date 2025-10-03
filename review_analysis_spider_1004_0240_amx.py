# 代码生成时间: 2025-10-04 02:40:19
import scrapy
def __init__(self):
    # 初始化spider，设置起始URL
    self.start_urls = ['http://example.com/reviews']

class ReviewAnalysisSpider(scrapy.Spider):
    # 定义爬虫
    name = 'review_analysis'
    allowed_domains = ['example.com']
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'DOWNLOAD_DELAY': 1,  # 避免IP被封锁
    }

    def parse(self, response):
        # 解析响应
        reviews = response.css('div.review::text').getall()
        for review in reviews:
            yield {
                'review': review.strip(),
            }

        # 找到下一页的链接并继续爬取
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def process_results(self, reviews):
        # 处理结果
        for review in reviews:
            print(review['review'])

        # 这里可以添加更多的分析逻辑，例如情感分析、关键词提取等

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # 从crawler中获取spider
        spider = super(ReviewAnalysisSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.process_results = cls.process_results
        return spider
