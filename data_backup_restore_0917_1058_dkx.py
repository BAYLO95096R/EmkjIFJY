# 代码生成时间: 2025-09-17 10:58:46
import os
import tarfile
import shutil
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging


# 配置日志
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})


class DataBackupSpider(Spider):
    name = "data_backup"
    allowed_domains = []  # 允许的域名列表
    start_urls = []     # 起始URL列表

    def __init__(self, backup=False, restore=False, backup_path='', restore_path='', *args, **kwargs):
        super(DataBackupSpider, self).__init__(*args, **kwargs)
        self.backup = backup
        self.restore = restore
        self.backup_path = backup_path
        self.restore_path = restore_path

    def start_requests(self):
        if self.backup:
            yield Request(url=self.backup_path, callback=self.backup_data)
        elif self.restore:
            yield Request(url=self.restore_path, callback=self.restore_data)
        else:
            self.logger.error("Neither backup nor restore operation is specified.")

    def backup_data(self, response):
        """备份数据文件到tar.gz格式"""
        try:
            tar = tarfile.open('backup.tar.gz', 'w:gz')
            tar.add(self.backup_path)
            tar.close()
            self.logger.info("Data backup successful.")
        except Exception as e:
            self.logger.error(f"Error during data backup: {e}")

    def restore_data(self, response):
        """从tar.gz格式恢复数据文件"""
        try:
            tar = tarfile.open('backup.tar.gz', 'r:gz')
            tar.extractall(path=self.restore_path)
            tar.close()
            self.logger.info("Data restore successful.")
        except Exception as e:
            self.logger.error(f"Error during data restore: {e}")
            shutil.rmtree(self.restore_path)  # 恢复失败时删除已解压的文件


# 主函数
def main():
    # 创建一个爬虫处理器
    process = CrawlerProcess()
    # 添加爬虫
    process.crawl(DataBackupSpider, backup=True, backup_path='/path/to/data/directory')
    # 开始爬取
    process.start()

    # 或者，恢复数据
    # process.crawl(DataBackupSpider, restore=True, restore_path='/path/to/restore/directory')
    # process.start()

if __name__ == '__main__':
    main()
