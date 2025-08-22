# 代码生成时间: 2025-08-22 17:37:59
import scrapy
aiohttp
from scrapy.crawler import CrawlerProcess
aiohttp
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.exceptions import CloseSpider
import logging

"""
User Login Spider

This spider is designed to simulate a user login verification system.
It sends a POST request with username and password to the specified login endpoint.
"""

class UserLoginSpider(Spider):
    name = 'user_login'
    allowed_domains = ['example.com']  # Replace with your actual domain
    start_urls = ['http://example.com/login']  # Replace with your actual login URL

    def __init__(self, username=None, password=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.password = password

    def parse(self, response):
        """
        Send a POST request with username and password to the login endpoint.
        If the login is successful, print the response.
        If the login fails, close the spider and log an error message.
        """
        login_url = response.url
        data = {
            'username': self.username,
            'password': self.password
        }
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        
        yield Request(
            url=login_url,
            method='POST',
            headers=headers,
            body=self.urlencode(data),
            callback=self.after_login
        )

    def after_login(self, response):
        """
        Handle the response after login.
        If the login is successful, print the response.
        If the login fails, log an error message and close the spider.
        """
        if response.status == 200:
            logging.info('Login successful')
            self.log('Login successful')
        else:
            logging.error('Login failed')
            self.log('Login failed', level=logging.ERROR)
            raise CloseSpider('Login failed')

    def urlencode(self, data):
        """
        Encode the data to a URL-encoded format.
        """
        if isinstance(data, dict):
            return '&'.join(f'{k}={v}' for k, v in data.items())
        return data

# Create a CrawlerProcess instance and start the spider
process = CrawlerProcess()
process.crawl(UserLoginSpider, username='your_username', password='your_password')
process.start()
