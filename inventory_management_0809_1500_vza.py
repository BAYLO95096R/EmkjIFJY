# 代码生成时间: 2025-08-09 15:00:10
import scrapy

"""
库存管理系统使用Scrapy框架进行数据抓取和存储。
这个脚本定义了一个Scrapy项目，用于抓取库存信息并存储至本地文件。
"""


class InventoryItem(scrapy.Item):
    """
    定义库存项的数据结构。
    """
    item_id = scrapy.Field()  # 物品ID
    name = scrapy.Field()     # 物品名称
    quantity = scrapy.Field()  # 物品数量
    price = scrapy.Field()    # 物品价格


class InventorySpider(scrapy.Spider):
    """
    库存管理系统的Scrapy爬虫。
    """
    name = 'inventory_spider'
    allowed_domains = ['example.com']  # 允许爬取的域名
    start_urls = ['http://example.com/inventory']  # 起始URL列表

    def parse(self, response):
        """
        解析库存页面，提取库存项信息。
        """
        for item in response.css('div.inventory-item'):
            item_data = InventoryItem()
            item_data['item_id'] = item.css('span.item-id::text').get()
            item_data['name'] = item.css('span.item-name::text').get()
            item_data['quantity'] = item.css('span.item-quantity::text').get()
            item_data['price'] = item.css('span.item-price::text').get()
            yield item_data

        # 处理翻页
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)


# 库存管理Pipeline，用于存储库存数据
class InventoryPipeline:
    def open_spider(self, spider):
        """
        打开spider时初始化文件存储。
        """
        self.file = open('inventory_data.json', 'w')

    def close_spider(self, spider):
        """
        关闭spider时关闭文件存储。
        """
        self.file.close()

    def process_item(self, item, spider):
        """
        处理每个库存项，将其存储到文件中。
        """
        self.file.write(f"{{"item_id":{item['item_id']},"name":"{item['name']}","quantity":{item['quantity']},"price":{item['price']}}},
")
        return item