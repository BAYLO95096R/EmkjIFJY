# 代码生成时间: 2025-08-02 10:25:31
import os
from PIL import Image
from scrapy import Spider, Request
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from scrapy.item import Field, Item
from scrapy.utils.response import open_in_browser
from scrapy.utils.python import to_bytes

# Define the item class for storing image file paths
class ImageItem(Item):
    image_paths = Field()

class ImageResizerSpider(Spider):
    name = "image_resizer"
    start_urls = []  # List of URLs to start scraping from
    resize_dimensions = (100, 100)  # Default resize dimensions

    def __init__(self, start_urls=None, resize_dimensions=None, *args, **kwargs):
# FIXME: 处理边界情况
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls or []
        self.resize_dimensions = resize_dimensions or (100, 100)

    def parse(self, response):
        # Check if the response contains image URLs
# NOTE: 重要实现细节
        if 'image' in response.headers.get('Content-Type', ''):
# 增强安全性
            # Directly process the image
            self.process_image(response.body)
        else:
            # Follow all links and process images found in subsequent pages
            for url in response.css('a::attr(href)').getall():
                yield Request(url, callback=self.parse)

    def process_image(self, image_bytes):
        # Open the image using PIL
# 改进用户体验
        try:
            with Image.open(image_bytes) as img:
                # Resize the image
                img = img.resize(self.resize_dimensions, Image.ANTIALIAS)
                # Create a temporary file to save the resized image
                temp_file = self.create_temp_file('.jpg')
                # Save the resized image to the temporary file
                img.save(temp_file, 'JPEG')
# 改进用户体验
                # Yield the image item with the temporary file path
                yield ItemLoader(item=ImageItem(), input_processor=lambda x: [x]).load_item()
                yield {"image_paths