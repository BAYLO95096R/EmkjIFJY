# 代码生成时间: 2025-09-22 15:31:45
import os
import shutil
from datetime import datetime
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.exceptions import NotConfigured


# 配置日志
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})


class FileBackupSyncSpider(Spider):
    name = "file_backup_sync"
    allowed_domains = []
    start_urls = []

    # 初始化时设置源目录和备份目录
    def __init__(self, source_dir, backup_dir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.backup_date = datetime.now().strftime("%Y%m%d%H%M%S")

    def start_requests(self):
        # 获取源目录下的所有文件和子目录
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.source_dir)
                backup_file_path = os.path.join(self.backup_dir, self.backup_date, relative_path)
                yield Request(url=file_path,
                                callback=self.backup_file,
                                meta={'source_path': file_path, 'backup_path': backup_file_path})

    def backup_file(self, response):
        """
        备份文件到指定目录
        :param response: Request response
        :param response.meta: {'source_path': source_file_path, 'backup_path': backup_file_path}
        """
        source_path = response.meta['source_path']
        backup_path = response.meta['backup_path']
        try:
            # 确保备份目录存在
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            # 复制文件
            shutil.copy2(source_path, backup_path)
            self.log('File backed up successfully: %s' % backup_path)
        except Exception as e:
            self.log('Error backing up file: %s' % e)

    def closed(self, reason):
        # 完成备份后的操作，例如清理
        self.log('Backup process completed. Reason: %s' % reason)


# 使用 Scrapy 运行爬虫
def run_spider(source_dir, backup_dir):
    try:
        process = CrawlerProcess()
        process.crawl(FileBackupSyncSpider, source_dir=source_dir, backup_dir=backup_dir)
        process.start()
    except NotConfigured as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')


if __name__ == '__main__':
    # 源目录和备份目录
    source_directory = '/path/to/source/directory'
    backup_directory = '/path/to/backup/directory'
    # 运行爬虫
    run_spider(source_directory, backup_directory)