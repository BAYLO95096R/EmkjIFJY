# 代码生成时间: 2025-08-12 03:56:40
import scrapy

# 定义一个购物车类
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    # 添加商品到购物车
    def add_product(self, product_id, quantity):
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity

    # 从购物车中移除商品
    def remove_product(self, product_id, quantity):
        if product_id in self.cart:
            if self.cart[product_id] <= quantity:
                del self.cart[product_id]
            else:
                self.cart[product_id] -= quantity
        else:
            raise ValueError("Product not found in the cart")

    # 获取购物车中所有商品的总数量
    def get_total_quantity(self):
        return sum(self.cart.values())

    # 获取购物车中所有商品的详情
    def get_cart_details(self):
        return self.cart

# 定义一个Scrapy Spider
class ShoppingCartSpider(scrapy.Spider):
    name = "shopping_cart_spider"
    allowed_domains = []  # 设置允许爬取的域名
    start_urls = []  # 设置起始URLs
    
    def __init__(self):
        self.cart = ShoppingCart()  # 初始化购物车

    def parse(self, response):
        # 解析页面内容
        # 这里假设页面包含了商品列表，每个商品有一个ID和数量
        products = response.xpath("//div[@class='product']")
        for product in products:
            product_id = product.xpath("./@data-id").get()
            quantity = int(product.xpath("./@data-quantity").get())
            try:
                self.cart.add_product(product_id, quantity)
            except ValueError as e:
                self.logger.error(f"Error adding product to cart: {e}")

    def closed(self, reason):
        # 在Spider关闭时执行的操作
        self.logger.info(f"Total quantity in cart: {self.cart.get_total_quantity()}")
        self.logger.info(f"Cart details: {self.cart.get_cart_details()}")
