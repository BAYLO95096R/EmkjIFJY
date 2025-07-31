# 代码生成时间: 2025-07-31 22:58:19
import os
import shutil
from scrapy.exceptions import NotConfigured

"""
A Scrapy spider that organizes the folder structure.
"""

class FolderStructureOrganizer:
    def __init__(self, source_folder, destination_folder):
        """
        Initialize the Folder Structure Organizer.

        :param source_folder: The path to the source folder.
        :param destination_folder: The path to the destination folder.
        """
        self.source_folder = source_folder
        self.destination_folder = destination_folder
        self.extensions_map = {
            'images': ['.jpg', '.jpeg', '.png', '.gif'],
            'documents': ['.pdf', '.doc', '.docx', '.txt'],
            'videos': ['.mp4', '.mov', '.avi'],
            'audios': ['.mp3', '.wav'],
            'archives': ['.zip', '.rar', '.7z']
        }

    def organize(self):
        """
        Organize the folder structure by moving files into their respective folders.
        """
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

        for root, dirs, files in os.walk(self.source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()

                for category, extensions in self.extensions_map.items():
                    if file_extension in extensions:
                        target_folder = os.path.join(self.destination_folder, category)
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)

                        target_path = os.path.join(target_folder, file)
                        shutil.move(file_path, target_path)
                        break

    def run(self):
        try:
            self.organize()
        except Exception as e:
            raise NotConfigured(f'Failed to organize folders: {e}')

# Example usage:
# organizer = FolderStructureOrganizer('/path/to/source', '/path/to/destination')
# organizer.run()
