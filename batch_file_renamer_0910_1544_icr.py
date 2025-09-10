# 代码生成时间: 2025-09-10 15:44:14
import os
from scrapy.exceptions import DropItem

class BatchFileRenamer:
    def __init__(self, directory):
        """
        Initialize the BatchFileRenamer with a directory to rename files in.

        :param directory: The directory to rename files in
        """
        self.directory = directory

    def rename_files(self, new_name_prefix):
        """
        Rename all files in the directory with a new name prefix.

        :param new_name_prefix: The prefix for the new file names
# NOTE: 重要实现细节
        """
        for filename in os.listdir(self.directory):
            try:
                # Construct the new file path with the new name prefix
                new_filename = f"{new_name_prefix}_{filename}"
                new_filepath = os.path.join(self.directory, new_filename)
                old_filepath = os.path.join(self.directory, filename)
# TODO: 优化性能

                # Rename the file
                os.rename(old_filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except OSError as e:
                # Handle file rename errors
                print(f"Error renaming file '{filename}': {e}")
                raise DropItem(f"Error renaming file '{filename}': {e}")
            except Exception as e:
                # Handle any other unexpected errors
                print(f"Unexpected error renaming file '{filename}': {e}")
                raise DropItem(f"Unexpected error renaming file '{filename}': {e}")

if __name__ == '__main__':
    # Example usage: rename all files in the current directory with prefix 'new_'
    directory = os.getcwd()
    renamer = BatchFileRenamer(directory)
    renamer.rename_files('new_')
