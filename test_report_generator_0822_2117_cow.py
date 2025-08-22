# 代码生成时间: 2025-08-22 21:17:26
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings
from scrapy.exporters import XmlItemExporter
from scrapy.item import Item, Field


# 定义测试报告项目
class TestReportItem(Item):
    # 定义Item字段
    name = Field()
    result = Field()
    error_message = Field()


# 定义测试报告生成器
class TestReportGenerator:
    def __init__(self, output_file):
        """初始化测试报告生成器

        Args:
            output_file (str): 输出文件路径
        """
        self.output_file = output_file

    def generate_report(self, results):
        """生成测试报告

        Args:
            results (list): 测试结果列表
        """
        # 创建一个Scrapy项目
        try:
            settings = get_project_settings()
        except NotConfigured:
            raise NotConfigured("未配置Scrapy项目")

        # 创建一个Scrapy爬虫
        process = CrawlerProcess(settings)

        # 创建一个ItemExporter，导出到XML文件
        exporter = XmlItemExporter(self.output_file)
        exporter.start_exporting()

        # 将测试结果转换为Item
        for result in results:
            item = TestReportItem()
            item["name"] = result["name"]
            item["result"] = result["result"]
            item["error_message"] = result.get("error_message", "")
            exporter.export_item(item)

        # 完成导出
        exporter.finish_exporting()


# 示例用法
if __name__ == "__main__":
    # 测试结果列表
    results = [
        {"name": "测试1", "result": "成功"},
        {"name": "测试2", "result": "失败", "error_message": "断言失败"},
        {"name": "测试3", "result": "成功"},
    ]

    # 创建一个测试报告生成器
    report_generator = TestReportGenerator("test_report.xml")

    # 生成测试报告
    report_generator.generate_report(results)
