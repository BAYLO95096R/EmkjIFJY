# 代码生成时间: 2025-08-02 05:01:00
import os
from PIL import Image
from scrapy import Spider, Request
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from scrapy.item import Field, Item
from scrapy.exceptions import DropItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

# Define the item structure for storing image file paths
class ImageItem(Item):
    image_urls = Field()
    images = Field()

# Define the spider
class ImageResizerSpider(Spider):
    name = 'image_resizer'
    allowed_domains = []  # List of allowed domains
    start_urls = []
    image_download_dir = './resized_images'  # Directory to store resized images

    def start_requests(self):
        # Send a request to each image URL to download it
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        # Extract image URLs from the response
        base_url = get_base_url(response)
        image_loader = ItemLoader(item=ImageItem(), response=response)
        image_urls = response.css('img::attr(src)').getall()
        image_loader.add_value('image_urls', [urljoin_rfc(base_url, url) for url in image_urls])
        yield image_loader.load_item()

    def parse_image(self, response: HtmlResponse, item: ImageItem):
        # Download image and resize it
        try:
            with open(item['image_urls'][0].split('/')[-1], 'wb') as f:
                f.write(response.body)
            image_path = os.path.join(self.image_download_dir, item['image_urls'][0].split('/')[-1])
            image = Image.open(image_path)
            # Resize the image to the desired size
            # Example dimensions: (800, 600)
            resized_image = image.resize((800, 600))
            resized_image.save(image_path)
            item['images'] = [image_path]
            return item
        except Exception as e:
            self.logger.error(f'Error processing image {item[