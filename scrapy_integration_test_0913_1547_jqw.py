# 代码生成时间: 2025-09-13 15:47:04
import unittest
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from my_spider import MySpider  # 假设你有一个名为my_spider.py的文件，其中定义了MySpider

"""
集成测试工具，用于测试Scrapy爬虫
"""

class ScrapyIntegrationTest(unittest.TestCase):
    def setUp(self):
        """设置测试环境"""
        self.settings = get_project_settings()
        self.process = CrawlerProcess(settings=self.settings)

    def test_spider(self):
        """测试Scrapy爬虫"""
        try:
            # 启动爬虫
            self.process.crawl(MySpider)
            # 运行爬虫直到完成
            self.process.start()
        except Exception as e:
            # 错误处理
            self.fail(f"An error occurred: {e}")

    def tearDown(self):
        """清理测试环境"""
        self.process.stop()

if __name__ == "__main__":
    unittest.main()
