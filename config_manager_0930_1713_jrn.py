# 代码生成时间: 2025-09-30 17:13:46
import json
from scrapy.exceptions import NotConfigured


class ConfigManager:
    """
    配置文件管理器，用于加载和存储配置文件。
    """
    def __init__(self, config_file):
        """
        初始化配置文件管理器。
        :param config_file: 配置文件路径。
        """
        self.config_file = config_file
        self.config_data = {}
        self.load_config()

    def load_config(self):
        """
        从文件加载配置数据。
        """
        try:
            with open(self.config_file, 'r') as f:
                self.config_data = json.load(f)
        except FileNotFoundError:
            raise NotConfigured(f"配置文件 {self.config_file} 不存在。")
        except json.JSONDecodeError:
            raise NotConfigured(f"配置文件 {self.config_file} 格式错误。")

    def get_config(self, key):
        """
        获取指定键的配置值。
        :param key: 配置键。
        :return: 配置值。
        """
        try:
            return self.config_data[key]
        except KeyError:
            raise NotConfigured(f"配置键 {key} 不存在。")

    def set_config(self, key, value):
        """
        设置指定键的配置值。
        :param key: 配置键。
        :param value: 配置值。
        """
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        """
        将配置数据保存到文件。
        """
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config_data, f, indent=4)
        except IOError:
            raise NotConfigured(f"无法写入配置文件 {self.config_file}。")

    def delete_config(self, key):
        """
        删除指定键的配置值。
        :param key: 配置键。
        """
        try:
            del self.config_data[key]
            self.save_config()
        except KeyError:
            raise NotConfigured(f"配置键 {key} 不存在。")
"