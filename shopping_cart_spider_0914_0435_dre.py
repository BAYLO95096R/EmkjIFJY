# 代码生成时间: 2025-09-14 04:35:16
import scrapy
def run_shopping_cart_spider():
    # 实例化一个购物车类
    cart = ShoppingCart()

    # 添加商品到购物车
    cart.add_item('product1', 1)
    cart.add_item('product2', 2)
    cart.add_item('product3', 3)

    # 移除商品
    cart.remove_item('product2')

    # 获取购物车中的商品总数
    total_items = cart.get_total_items()
    print(f'Total items in cart: {total_items}')

    # 清空购物车
    cart.clear()

    # 检查购物车是否为空
    if cart.is_empty():
        print('Shopping cart is empty.')


# 购物车类
class ShoppingCart:
    def __init__(self):
        """
        初始化一个空购物车。
        """
        self.items = {}

    def add_item(self, item, quantity):
        """
        向购物车中添加商品。
        :param item: 商品名称
        :param quantity: 商品数量
        """
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        """
        从购物车中移除商品。
        :param item: 商品名称
        """
        if item in self.items:
            del self.items[item]
        else:
            print(f'Item {item} not found in cart.')

    def get_total_items(self):
        """
        获取购物车中的商品总数。
        :return: 商品总数
        """
        return sum(self.items.values())

    def clear(self):
        """
        清空购物车。
        """
        self.items = {}

    def is_empty(self):
        """
        检查购物车是否为空。
        :return: 如果购物车为空则返回True，否则返回False
        """
        return len(self.items) == 0


if __name__ == '__main__':
    run_shopping_cart_spider()