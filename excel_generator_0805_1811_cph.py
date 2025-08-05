# 代码生成时间: 2025-08-05 18:11:14
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
import pandas as pd
from openpyxl import Workbook
import logging

# 配置日志
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


class ExcelGenerator:
    """Excel表格自动生成器"""

    def __init__(self, data_source, output_file):
        "