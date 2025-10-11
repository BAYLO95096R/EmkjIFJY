# 代码生成时间: 2025-10-11 20:37:58
import os
import requests
from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.utils.misc import load_object
from scrapy.utils.python import to_bytes
from w3lib.url import safe_url_string"""
A Scrapy extension that provides OAuth2 authentication services.
"""

class OAuth2Service:
    def __init__(self, name, settings):
        # Load required settings for OAuth2
        self.client_id = settings.get('OAUTH2_CLIENT_ID')
        self.client_secret = settings.get('OAUTH2_CLIENT_SECRET')
        self.auth_url = settings.get('OAUTH2_AUTH_URL')
        self.token_url = settings.get('OAUTH2_TOKEN_URL')
        self.refresh_url = settings.get('OAUTH2_REFRESH_URL')
        self.scope = settings.get('OAUTH2_SCOPE')
        
        # Check if all required settings are available
        if not all([self.client_id, self.client_secret, self.auth_url, self.token_url, self.refresh_url, self.scope]):
            raise NotConfigured('OAuth2 settings are not configured properly.')

        # Initialize the access token
        self.access_token = None
        self.refresh_token = None
        self.expiry_time = 0

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create instances of the extension
        instance = cls(crawler.settings)
        crawler.signals.connect(instance._spider_opened, signal=signals.spider_opened)
        return instance

    def _spider_opened(self, spider):
        # Refresh the access token when a spider is opened
        self.refresh_access_token()

    def refresh_access_token(self):
        # Refresh the access token if it's expired or if it doesn't exist
        if self.access_token is None or self.is_token_expired():
            self.get_new_access_token()
        else:
            # Save the current access token for reuse
            self.save_access_token()

    def is_token_expired(self):
        # Check if the access token has expired
        current_time = time.time()
        return current_time >= self.expiry_time

    def get_new_access_token(self):
        # Get a new access token using the refresh token
        try:
            # Send a POST request to the token URL with the refresh token
            response = requests.post(self.token_url, data={
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
                'client_id': self.client_id,
                'client_secret': self.client_secret
            })
            response.raise_for_status()
            
            # Parse the response to get the new access token and its expiry time
            data = response.json()
            self.access_token = data['access_token']
            self.expiry_time = data['expires_in'] + time.time()
            
            # Save the new access token
            self.save_access_token()
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            self.logger.error(f'Error refreshing access token: {e}')

    def save_access_token(self):
        # Save the access token to a file for future use
        try:
            with open('access_token.txt', 'w') as f:
                f.write(self.access_token)
        except IOError as e:
            self.logger.error(f'Error saving access token: {e}')

    def get_auth_header(self):
        # Return the Authorization header with the access token
        if self.access_token is not None:
            return {'Authorization': f'Bearer {self.access_token}'}
        else:
            self.logger.error('Access token is not available.')
            return None
