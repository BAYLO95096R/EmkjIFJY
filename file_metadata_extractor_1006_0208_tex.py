# 代码生成时间: 2025-10-06 02:08:26
import os
from scrapy import signals
from scrapy.exceptions import NotConfigured

"""
File Metadata Extractor
This Scrapy extension allows to extract metadata from files
during the spider crawling process.
"""

class FileMetadataExtractor:
    def __init__(self, stats):
        self.stats = stats
        self.metadata = {}

    def extract_metadata(self, response, file_path, file_name):
        """
        Extract metadata from a file and store it in the stats.
        :param response: The response from which the file was downloaded.
        :param file_path: The path where the file was downloaded.
        :param file_name: The name of the file.
        :return: A dictionary containing the file metadata.
        """
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Get the file size
        file_size = os.path.getsize(file_path)

        # Get the file extension
        file_extension = os.path.splitext(file_name)[1]

        # Get the file creation and modification times
        creation_time = os.path.getctime(file_path)
        modification_time = os.path.getmtime(file_path)

        # Store the metadata in the stats
        self.metadata[file_name] = {
            'size': file_size,
            'extension': file_extension,
            'creation_time': creation_time,
            'modification_time': modification_time
        }

        # Return the metadata
        return self.metadata[file_name]

    def get_metadata(self):
        """
        Get the extracted metadata.
        :return: A dictionary containing all the extracted metadata.
        """
        return self.metadata

class FileMetadataExtractorExtension:
    def __init__(self, stats):
        self.stats = stats
        self.file_metadata_extractor = FileMetadataExtractor(stats)

    @classmethod
    def from_crawler(cls, crawler):
        """
        This method is used by Scrapy to create your spiders.
        :param crawler: The Scrapy crawler instance.
        :return: An instance of your class, or None if it was already created.
        """
        ext = cls(crawler.stats)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_closed(self):
        """
        Called when the spider is closed.
        """
        metadata = self.file_metadata_extractor.get_metadata()
        if metadata:
            self.stats.set_value('file_metadata', metadata)

# Example usage in a Scrapy spider
class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.com']

    def start_requests(self):
        yield scrapy.Request(url='https://example.com/file', callback=self.parse)

    def parse(self, response):
        file_path = '/path/to/downloaded/file'
        file_name = 'example.txt'
        try:
            metadata = self.crawler.extensions.get(FileMetadataExtractorExtension).file_metadata_extractor.extract_metadata(
                response, file_path, file_name)
            print(metadata)
        except FileNotFoundError as e:
            print(e)
            self.logger.error(e)
        