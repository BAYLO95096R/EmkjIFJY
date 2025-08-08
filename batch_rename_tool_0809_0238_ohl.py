# 代码生成时间: 2025-08-09 02:38:15
import os
import re
from scrapy.utils.project import get_project_settings

def rename_files(directory, pattern, replacement):
    """批量重命名目录中的文件。

    参数:
    directory: 需要重命名文件的目录路径。
    pattern: 需要匹配的正则表达式模式。
    replacement: 用于替换匹配部分的字符串。
    """
    try:
        # 检查目录是否存在
        if not os.path.exists(directory):
            raise FileNotFoundError(f"目录 {directory} 不存在。")
        
        # 遍历目录中的所有文件
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                # 使用正则表达式替换文件名中的匹配部分
                new_filename = re.sub(pattern, replacement, filename)
                # 构造新的文件路径
                new_filepath = os.path.join(directory, new_filename)
                # 重命名文件
                os.rename(filepath, new_filepath)
                print(f"文件 {filename} 已重命名为 {new_filename}。")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    # 定义目录路径、匹配模式和替换字符串
    directory_path = "/path/to/your/directory"
    pattern = "old_pattern"  # 正则表达式模式
    replacement = "new_pattern"  # 替换字符串

    # 调用函数进行批量重命名
    rename_files(directory_path, pattern, replacement)