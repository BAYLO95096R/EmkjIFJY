# 代码生成时间: 2025-09-08 16:31:01
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import NotConfigured

# 定义图表生成器类
class ChartGenerator:
    def __init__(self):
        self.process = CrawlerProcess(get_project_settings())
        self.charts = []

    # 启动爬虫
    def start(self):
        try:
            self.process.start()
        except NotConfigured as e:
            print(f"Error: {e}")

    # 添加图表
    def add_chart(self, chart_url):
        try:
            # 假设我们有一个用于获取图表的爬虫
            from chart_spider import ChartSpider
            self.process.crawl(ChartSpider, url=chart_url)
            self.charts.append(chart_url)
        except Exception as e:
            print(f"Error adding chart: {e}")

    # 生成图形
    def generate_charts(self):
        # 此处应有生成图表的代码
        # 由于SCRAPY框架主要用于爬虫，实际图表生成可能需要其他库如matplotlib或plotly
        # 因此这里只模拟图表生成的过程
        for chart_url in self.charts:
            print(f"Generating chart for: {chart_url}")
            # 模拟图表生成
            # 实际代码中这里将调用图表生成库的API

    # 停止爬虫
    def stop(self):
        self.process.stop()

# 定义交互式图表生成器的入口点
def main():
    chart_generator = ChartGenerator()
    chart_generator.start()
    try:
        while True:
            url = input("Enter chart URL (or 'exit' to quit): ")
            if url.lower() == 'exit':
                break
            chart_generator.add_chart(url)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        chart_generator.generate_charts()
        chart_generator.stop()

if __name__ == '__main__':
    main()