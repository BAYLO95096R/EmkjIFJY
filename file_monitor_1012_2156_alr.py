# 代码生成时间: 2025-10-12 21:56:52
import os
import time
from scrapy import signals
from scrapy.extensions.extension import Extension


# 用于存储文件的最新状态
class FileMonitor(Extension):
    def __init__(self, stats, files=None):
        super(FileMonitor, self).__init__()
        self.stats = stats
        self.files = files or []
        self.last_modification_times = {}

    def setup(self):
        # 记录文件最初的修改时间
        for file_path in self.files:
            self.last_modification_times[file_path] = self.get_file_modification_time(file_path)

    def get_file_modification_time(self, file_path):
        """获取文件的最后修改时间戳"""
        try:
            return os.path.getmtime(file_path)
        except OSError:
            # 文件不存在或无法访问时，记录错误
            self.stats.inc_value('file_monitor/missing_file', spider=spider)
            return None

    def check_files(self):
        """检查文件是否有变更，并通知"""
        for file_path in self.files:
            current_time = self.get_file_modification_time(file_path)
            if current_time and current_time != self.last_modification_times.get(file_path, None):
                self.stats.inc_value('file_monitor/changed_file', spider=spider)
                # 通知文件变更
                self.notify_file_change(file_path)
                # 更新记录的修改时间
                self.last_modification_times[file_path] = current_time

    def notify_file_change(self, file_path):
        """文件变更通知逻辑"""
        # 实际项目中可以替换为发送邮件、日志记录等通知方式
        print(f"File {file_path} has changed.")

    def close(self, reason):
        # 在关闭时可以添加清理逻辑
        pass


# Scrapy的信号处理器
class FileMonitorSpider(scrapy.Spider):
    name = 'file_monitor_spider'
    custom_settings = {
        'EXTENSIONS': {'file_monitor.FileMonitor': 1},
        'FILES': ['/path/to/your/file.txt'],
        'DOWNLOAD_DELAY': 0.5  # 减少请求间隔，加快监控频率
    }

    def start_requests(self):
        """启动监控文件的请求"""
        while not self.settings.getbool('CLOSESPIDER_ITEMCOUNT'):
            self.crawler.stats.set_value('file_monitor/last_run', time.time())
            self.crawler.extensions.get('file_monitor.FileMonitor').check_files()
            time.sleep(1)  # 暂停1秒后再检查文件


# 请注意，这个脚本是一个示例，需要结合Scrapy框架使用，并且需要配置Scrapy项目和相应的文件路径。
# 此外，这个脚本的`close`方法和`notify_file_change`方法需要根据实际需求进行扩展和实现。