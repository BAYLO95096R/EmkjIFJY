# 代码生成时间: 2025-08-11 18:15:17
import os
from scrapy import Spider, Request

"""
批量文件重命名工具，用于将指定目录下的文件按照一定规则重新命名。

参数：
- source_dir: 要重命名的文件所在的目录
- dest_dir: 重命名后文件存放的目录
- rename_rule: 重命名规则函数，输入旧文件名，返回新文件名

使用示例：
    rename_files('source_folder', 'destination_folder', lambda x: x.replace('old', 'new'))
"""

class BulkRenameTool:
    def __init__(self, source_dir, dest_dir, rename_rule):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.rename_rule = rename_rule

    def rename_files(self):
        """执行文件重命名操作"""
        if not os.path.exists(self.dest_dir):
            os.makedirs(self.dest_dir)

        for filename in os.listdir(self.source_dir):
            old_file_path = os.path.join(self.source_dir, filename)
            new_filename = self.rename_rule(filename)
            new_file_path = os.path.join(self.dest_dir, new_filename)

            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{old_file_path}' to '{new_file_path}'")
            except OSError as e:
                print(f"Error renaming '{old_file_path}' to '{new_file_path}': {e}
")

# 使用示例
if __name__ == '__main__':
    source_dir = 'path/to/source/directory'
    dest_dir = 'path/to/destination/directory'
    rename_rule = lambda x: x.replace('old_extension', 'new_extension')

    rename_tool = BulkRenameTool(source_dir, dest_dir, rename_rule)
    rename_tool.rename_files()