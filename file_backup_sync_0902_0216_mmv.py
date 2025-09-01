# 代码生成时间: 2025-09-02 02:16:29
import os
import shutil
from scrapy.utils.project import get_project_settings

"""
文件备份和同步工具
用于备份和同步指定目录中的文件
"""

class FileBackupSync:
    def __init__(self, source_dir, backup_dir):
        """
        初始化文件备份和同步工具
        :param source_dir: 源目录路径
        :param backup_dir: 备份目录路径
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        self.settings = get_project_settings()

    def backup_files(self):
        """
        备份源目录中的文件到备份目录
        """
        try:
            if not os.path.exists(self.backup_dir):
                os.makedirs(self.backup_dir)
            for filename in os.listdir(self.source_dir):
                source_file_path = os.path.join(self.source_dir, filename)
                backup_file_path = os.path.join(self.backup_dir, filename)
                if os.path.isfile(source_file_path):
                    shutil.copy2(source_file_path, backup_file_path)
            print(f"文件备份完成：{self.backup_dir}")
        except Exception as e:
            print(f"备份文件时发生错误：{e}")

    def sync_files(self):
        """
        同步源目录和备份目录中的文件
        """
        try:
            source_files = set(os.listdir(self.source_dir))
            backup_files = set(os.listdir(self.backup_dir))
            files_to_add = source_files - backup_files
            files_to_remove = backup_files - source_files

            for filename in files_to_add:
                source_file_path = os.path.join(self.source_dir, filename)
                backup_file_path = os.path.join(self.backup_dir, filename)
                shutil.copy2(source_file_path, backup_file_path)
                print(f"同步文件：{filename}")

            for filename in files_to_remove:
                backup_file_path = os.path.join(self.backup_dir, filename)
                os.remove(backup_file_path)
                print(f"删除文件：{filename}")

            print(f"文件同步完成：{self.backup_dir}")
        except Exception as e:
            print(f"同步文件时发生错误：{e}")

# 示例用法
if __name__ == "__main__":
    source_dir = "/path/to/source/directory"
    backup_dir = "/path/to/backup/directory"

    file_backup_sync = FileBackupSync(source_dir, backup_dir)
    file_backup_sync.backup_files()
    file_backup_sync.sync_files()