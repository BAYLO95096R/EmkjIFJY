# 代码生成时间: 2025-08-23 19:09:19
import os
import shutil
import hashlib
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.exceptions import NotConfigured

# 配置日志
configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})


class FileBackupSync(Spider):
    name = 'file_backup_sync'
# TODO: 优化性能
    allowed_domains = []
    start_urls = []

    # 构造函数，初始化源目录和目标目录
# 扩展功能模块
    def __init__(self, source_dir, target_dir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.files_to_sync = {}
# 扩展功能模块

    # 开始爬取
    def start_requests(self):
        for root, dirs, files in os.walk(self.source_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                self.files_to_sync[file_path] = self.get_file_hash(file_path)
                yield Request(url=file_path, callback=self.sync_file)

    # 计算文件的哈希值
    def get_file_hash(self, file_path):
        with open(file_path, 'rb') as file:
            return hashlib.sha256(file.read()).hexdigest()

    # 同步文件
    def sync_file(self, response):
        file_path = response.url
        file_name = os.path.basename(file_path)
# 改进用户体验
        target_file_path = os.path.join(self.target_dir, file_name)

        # 检查目标目录是否存在，如果不存在则创建
        if not os.path.exists(self.target_dir):
# 改进用户体验
            os.makedirs(self.target_dir)

        # 计算目标文件的哈希值
        target_file_hash = self.get_file_hash(target_file_path) if os.path.exists(target_file_path) else None

        # 如果哈希值不同，则同步文件
        if target_file_hash != self.files_to_sync[file_path]:
# 扩展功能模块
            try:
# NOTE: 重要实现细节
                shutil.copy2(file_path, target_file_path)
                self.logger.info(f"File {file_name} synced successfully")
            except Exception as e:
                self.logger.error(f"Error syncing file {file_name}: {str(e)}")
        else:
            self.logger.info(f"File {file_name} is already up-to-date")


# 主函数
def main():
    source_dir = input("Enter source directory: ")
    target_dir = input("Enter target directory: ")
    process = CrawlerProcess()
    process.crawl(FileBackupSync, source_dir=source_dir, target_dir=target_dir)
    process.start()

if __name__ == '__main__':
# NOTE: 重要实现细节
    main()