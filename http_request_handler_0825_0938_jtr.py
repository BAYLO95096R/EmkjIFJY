# 代码生成时间: 2025-08-25 09:38:28
import scrapy
def http_request_handler(url):
    """
    HTTP请求处理器，用于发送GET请求并返回响应。
    
    参数:
        url (str): 需要发送请求的URL。
    
    返回:
        response (scrapy.http.Response): 请求的响应对象。
    """
    try:
        # 创建Scrapy请求对象
        request = scrapy.Request(url)
        # 发送请求
        response = scrapy.Spider().fetch(request)
        
        # 检查响应状态码
        if response.status != 200:
            raise Exception(f"请求失败，状态码：{response.status}")
        
        return response
    except Exception as e:
        # 错误处理
        print(f"请求过程中发生错误：{e}")
        return None

# 测试代码
if __name__ == '__main__':
    url = "http://example.com"
    response = http_request_handler(url)
    if response:
        print("请求成功，响应内容：")
        print(response.body)
    else:
        print("请求失败")