# 代码生成时间: 2025-08-24 01:18:43
import scrapy
def run_spider(spider_name):
    # 导入Scrapy Spider
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    from scrapy.utils.spider import spidercls_for_name

    # 设置函数
    def settings_func():
        return get_project_settings()

    # 创建爬虫进程
    process = CrawlerProcess(settings_func=settings_func())

    # 获取并启动Spider
    spider_cls = spidercls_for_name(spider_name, settings_func())
    process.crawl(spider_cls)
    process.start()

    # 错误处理
    except Exception as e:
        print(f"An error occurred: {e}")


# 主函数，用于运行程序
if __name__ == "__main__":
    import sys

    # 检查命令行参数
    if len(sys.argv) != 2:
        print("Usage: python process_manager_scrapy.py <spider_name>")
        sys.exit(1)

    # 获取Spider名称
    spider_name = sys.argv[1]

    # 调用run_spider函数
    run_spider(spider_name)