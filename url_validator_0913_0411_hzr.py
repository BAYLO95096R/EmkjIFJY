# 代码生成时间: 2025-09-13 04:11:32
import scrapy
def validate_url(url):
    # 验证URL是否有效
    try:
        from urllib.parse import urlparse
        result = urlparse(url)
        # 检查是否具有网络位置部分
        if all([result.scheme, result.netloc]):
            return True
        else:
            return False
    except ValueError:
        # 如果解析URL失败，则返回False
        return False

def main():
    # 测试URL链接有效性
    urls_to_test = [
        "http://www.example.com",
        "https://www.google.com",
        "ftp://example.com",
        "not-a-valid-url"
    ]
    for url in urls_to_test:
        is_valid = validate_url(url)
        print(f"URL: {url} is valid: {is_valid}")

if __name__ == "__main__":
    main()
