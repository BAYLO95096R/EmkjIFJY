# 代码生成时间: 2025-08-06 15:20:15
import scrapy
def get_web_content(url):
    """
    使用Scrapy框架的CrawlSpider抓取指定网页的内容。

    Args:
    url (str): 要抓取的网页地址。

    Returns:
    str: 网页内容。
    """
    class WebContentSpider(scrapy.Spider):
        name = "web_content_spider"
        start_urls = [url]

        def parse(self, response):
            try:
                # 处理响应，提取网页内容
# 扩展功能模块
                content = response.text
                return {"url": response.url, "content": content}
            except Exception as e:
                # 如果处理过程中出现错误，返回错误信息
# 扩展功能模块
                return {"error": str(e)}

    # 使用Scrapy的运行时创建并运行爬虫
    runner = scrapy.crawler.CrawlerRunner()
    d = runner.crawl(WebContentSpider)
    results = runner.join()
    
    # 从爬虫结果中提取网页内容
    if results:
        return results[0]
# 扩展功能模块
    else:
        return {"error": "No results found"}

# 示例用法
if __name__ == "__main__":
    url = "http://example.com"
    result = get_web_content(url)
    print(result)