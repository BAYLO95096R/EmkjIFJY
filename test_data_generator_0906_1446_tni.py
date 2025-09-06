# 代码生成时间: 2025-09-06 14:46:45
import json
from scrapy.http import HtmlResponse
from scrapy.item import Item, Field
from scrapy.spiders import Spider
import random
import string
import scrapy.exceptions


# 定义一个Item，用于存储生成的测试数据
class TestDataItem(Item):
    name = Field()
    email = Field()
    age = Field()


# 测试数据生成器类
class TestDataGenerator:
    def __init__(self, num_records):
        """
        初始化测试数据生成器

        :param num_records: 要生成的测试数据记录数
        """
        self.num_records = num_records

    def generate(self):
        """
        生成测试数据

        :return: 生成的测试数据列表
        """
        test_data = []
        for _ in range(self.num_records):
            name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
            email = f"{name}@example.com"
            age = random.randint(18, 100)
            test_data.append(TestDataItem(name=name, email=email, age=age))
        return test_data

    def save_to_file(self, file_path):
        """
        将生成的测试数据保存到文件

        :param file_path: 文件路径
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.generate(), f)
        except IOError as e:
            raise scrapy.exceptions.CloseSpider(f"Failed to save test data to file: {e}")


# Scrapy Spider，用于调用测试数据生成器并保存生成的数据
class TestDataSpider(Spider):
    name = 'test_data_spider'

    def __init__(self, num_records=100, file_path='test_data.json', *args, **kwargs):
        super(TestDataSpider, self).__init__(*args, **kwargs)
        self.num_records = num_records
        self.file_path = file_path
        self.generator = TestDataGenerator(self.num_records)

    def start_requests(self):
        """
        开始请求，生成测试数据并保存到文件
        """
        try:
            self.generator.save_to_file(self.file_path)
            self.log(f"Test data generated and saved to {self.file_path}")
        except Exception as e:
            self.log(f"Error generating test data: {e}", level=logging.ERROR)

    def parse(self, response):
        """
        解析响应（在这个Spider中不需要）
        """
        return []
