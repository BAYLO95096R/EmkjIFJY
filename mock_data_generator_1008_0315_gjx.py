# 代码生成时间: 2025-10-08 03:15:25
import json
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import CloseSpider

class MockDataGenerator:
    """
    A class to generate mock data for Scrapy spiders.
    This class can be used to populate a Scrapy item pipeline with mock data,
    allowing for testing and development without actually scraping websites.
    """

    def __init__(self, num_items=100, data_template=None):
        """
        Initializes the MockDataGenerator with the number of items to generate and a template for the data.
        :param num_items: The number of mock items to generate (default is 100).
        :param data_template: A dictionary template for the mock data (default is None, use default template).
        """
        self.num_items = num_items
        self.data_template = data_template or self._get_default_template()

    def _get_default_template(self):
        """
        Returns a default template for mock data.
        """
        return {
            'id': lambda: self._generate_random_id(),
            'title': lambda: self._generate_random_string(10),
            'description': lambda: self._generate_random_string(100),
            'price': lambda: round(self._generate_random_number(100, 1000), 2),
        }

    def _generate_random_id(self):
        """
        Generates a random ID.
        """
        import random
        return random.randint(1000, 9999)

    def _generate_random_string(self, length):
        """
        Generates a random string of a given length.
        """
        import random
        import string
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def _generate_random_number(self, min_value, max_value):
        """
        Generates a random number within a given range.
        """
        import random
        return random.uniform(min_value, max_value)

    def generate(self):
        """
        Generates the mock data.
        :returns: A list of mock data items.
        """
        mock_data = []
        for _ in range(self.num_items):
            item = {key: func() for key, func in self.data_template.items()}
            mock_data.append(item)
        return mock_data

    def save_to_file(self, file_path):
        """
        Saves the mock data to a file.
        :param file_path: The path to the file where the mock data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.generate(), file, indent=4)
        except IOError as e:
            raise CloseSpider(f"Failed to write to file: {e}")

# Example usage
if __name__ == '__main__':
    settings = get_project_settings()
    mock_generator = MockDataGenerator(num_items=50)
    mock_data = mock_generator.generate()
    print(mock_data)  # Print the mock data
    # mock_generator.save_to_file('mock_data.json')  # Uncomment to save to file
