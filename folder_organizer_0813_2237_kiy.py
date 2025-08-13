# 代码生成时间: 2025-08-13 22:37:28
import os
import shutil
from scrapy.exceptions import NotConfigured

"""
A Scrapy Spider that organizes a directory structure.
It moves files to their respective folders based on a predefined rule.
"""

class FolderOrganizer:
    def __init__(self, folder_path):
        """
        Initialize the FolderOrganizer with a path to the folder to organize.
        :param folder_path: Path to the folder that needs organizing.
        If not provided, the current working directory is used.
        """
        self.folder_path = folder_path or os.getcwd()
        self.rules = {
            '.pdf': 'Documents',
            '.jpg': 'Images',
            '.jpeg': 'Images',
            '.png': 'Images',
            '.mp3': 'Music',
            '.mp4': 'Videos',
            '.txt': 'Texts',
            '.py': 'Code'
        }

    def organize(self):
        "