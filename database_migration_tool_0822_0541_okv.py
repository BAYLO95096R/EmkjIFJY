# 代码生成时间: 2025-08-22 05:41:27
import logging
from scrapy import Spider, signals
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from your_project.models import Base, YourModel  # Import your database model


class DatabaseMigrationTool(Spider):
    name = 'database_migration_tool'
    allowed_domains = []
    start_urls = []

    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Check if the required settings are provided
        if not get_project_settings().get('DB_MIGRATION_SETTINGS'):
            raise NotConfigured('Missing required DB_MIGRATION_SETTINGS')
        
        # Set up database connection
        try:
            self.engine = create_engine(get_project_settings().get('DB_MIGRATION_SETTINGS')['DATABASE_URL'])
            self.Session = sessionmaker(bind=self.engine)
        except SQLAlchemyError as e:
            self.logger.error(f'Database connection error: {e}')
            raise NotConfigured('Database connection could not be established')
        
        # Bind the close spider signal to the session close method
        self.crawler.signals.connect(self.close_session, signal=signals.spider_closed)
        
        # Call the parent's init method
        super().__init__()

    def close_session(self):
        """Close the database session when the spider is closed."""
        self.Session.close_all()

    def start_requests(self):
        "