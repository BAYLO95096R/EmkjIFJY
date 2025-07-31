# 代码生成时间: 2025-07-31 11:41:52
import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured

"""
一个简单的Scrapy错误日志收集器扩展。
这个扩展将捕获Scrapy产生的所有错误信息，并将其记录到日志文件中。
"""

class ErrorLogCollector:
    """错误日志收集器"""
    def __init__(self, stats):
        # 初始化时，设置日志配置
        self.logger = logging.getLogger(__name__)
        # 检查是否配置了日志文件路径
        if not stats.get('error_log_file'):
            raise NotConfigured("需要配置error_log_file参数")
# FIXME: 处理边界情况
        self.error_log_file = stats.get('error_log_file')
        # 设置日志记录器的级别和文件处理器
        handler = logging.FileHandler(self.error_log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.ERROR)
        self.logger.propagate = False

    def spider_opened(self, spider):
        """当spider打开时，注册信号处理器。"""
# TODO: 优化性能
        # 注册spider错误处理信号
        spider.crawler.signals.connect(self.spider_error, signal=signals.spider_error)

    def spider_error(self, failure, response, spider):
        """处理spider错误。"""
        # 检查failure是否不为空
        if failure:
            # 记录错误信息
            self.logger.error(f'Error on {spider.name}: {failure.value}')


# 配置示例
# 在settings.py文件中添加以下配置
# ERROR_LOG_FILE = '/path/to/your/error.log'
# EXTENSIONS = {'error_log_collector.ErrorLogCollector': 500}
# EXTENSION_ORDER = {'error_log_collector.ErrorLogCollector': 500}
