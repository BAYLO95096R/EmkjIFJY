# 代码生成时间: 2025-08-29 02:45:29
import os
import zipfile
import tarfile
from io import BytesIO

"""
A utility class for decompressing files using Python.
This class provides a simple interface to extract files from various compression formats.
"""

class Decompressor:
    def __init__(self):
        """
        Initialize the Decompressor class.
        """
        pass

    def unzip(self, file_path):
        """
        Decompress a ZIP file.

        Args:
            file_path (str): The path to the ZIP file to decompress.

        Returns:
            bool: True if decompression succeeds, False otherwise.
        """
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(file_path))
                return True
        except Exception as e:
            print(f"An error occurred while unzipping: {e}")
            return False

    def untar(self, file_path):
        """
        Decompress a TAR file.

        Args:
            file_path (str): The path to the TAR file to decompress.

        Returns:
            bool: True if decompression succeeds, False otherwise.
        """
        try:
            with tarfile.open(file_path, 'r') as tar_ref:
                tar_ref.extractall(os.path.dirname(file_path))
                return True
        except Exception as e:
            print(f"An error occurred while untarring: {e}")
            return False

    def decompress(self, file_path):
        """
        Decompress a file based on its extension.

        Args:
            file_path (str): The path to the file to decompress.

        Returns:
            bool: True if decompression succeeds, False otherwise.
        """
        if file_path.endswith('.zip'):
            return self.unzip(file_path)
        elif file_path.endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2')):
            return self.untar(file_path)
        else:
            print("Unsupported file type.")
            return False

# Example usage
if __name__ == '__main__':
    Decompressor = Decompressor()
    file_path = 'path_to_your_compressed_file'
    result = Decompressor.decompress(file_path)
    if result:
        print(f"File {file_path} has been decompressed successfully.")
    else:
        print(f"Failed to decompress file {file_path}.")