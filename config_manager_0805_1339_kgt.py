# 代码生成时间: 2025-08-05 13:39:44
import json
from scrapy.exceptions import NotConfigured


# Configuration Manager for Scrapy
class ConfigManager:
    """
    Manages configuration settings for Scrapy projects.
    This class allows for loading, saving, and editing of configuration files.
    """

    def __init__(self, config_file='settings.json'):
        """
        Initializes the ConfigManager with a specified configuration file.
        """
        self.config_file = config_file
        self.config_data = {}
        self.load_config()

    def load_config(self):
        """
        Loads the configuration from the file.
        Raises NotConfigured if the file does not exist or is inaccessible.
        """
        try:
            with open(self.config_file, 'r') as file:
                self.config_data = json.load(file)
        except FileNotFoundError:
            raise NotConfigured(f"Configuration file '{self.config_file}' not found.")
        except json.JSONDecodeError:
            raise NotConfigured(f"Error parsing configuration file '{self.config_file}'.")

    def save_config(self):
        """
        Saves the current configuration to the file.
        """
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file, indent=4)

    def get_config(self, key):
        """
        Retrieves a configuration value by key.
        Returns None if the key does not exist.
        """
        return self.config_data.get(key)

    def set_config(self, key, value):
        """
        Sets a configuration value by key.
        """
        self.config_data[key] = value
        self.save_config()  # Automatically save changes

    def delete_config(self, key):
        """
        Deletes a configuration value by key.
        Raises KeyError if the key does not exist.
        """
        if key in self.config_data:
            del self.config_data[key]
            self.save_config()  # Automatically save changes
        else:
            raise KeyError(f"Configuration key '{key}' not found.")


# Example usage:
if __name__ == '__main__':
    config_manager = ConfigManager()
    try:
        # Load configuration
        config_manager.load_config()
        
        # Set a new configuration value
        config_manager.set_config('MY_SETTING', 'my_value')
        
        # Get a configuration value
        print(config_manager.get_config('MY_SETTING'))
        
        # Delete a configuration value
        config_manager.delete_config('MY_SETTING')
    except NotConfigured as e:
        print(f'Error: {e}')
