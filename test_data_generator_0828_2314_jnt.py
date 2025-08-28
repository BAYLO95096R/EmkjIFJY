# 代码生成时间: 2025-08-28 23:14:05
import scrapy
from scrapy.item import Field, Item
import random
import json

def generate_test_data(num_records, output_file):
    # Define the Item structure for the test data
    class TestDataItem(Item):
        name = Field()
        email = Field()
        age = Field()
    
    def generate_random_email():
        """Generate a random email."""
        return f"{random.randint(100000, 999999)}@example.com"
    
    def generate_random_name():
        """Generate a random name."""
        names = ["John", "Alice", "Bob", "Eve"]
        return random.choice(names)
    
    def generate_random_age():
        """Generate a random age between 18 and 90."""
        return random.randint(18, 90)
    
    try:
        test_data_list = []
        # Generate the specified number of test records
        for _ in range(num_records):
            item = TestDataItem(
                name=generate_random_name(),
                email=generate_random_email(),
                age=generate_random_age()
            )
            test_data_list.append(item)
        
        # Write the test data to the output file in JSON format
        with open(output_file, 'w') as f:
            json.dump([{field: item[field] for field in item.fields} for item in test_data_list], f, indent=4)
        print(f"Test data generated successfully and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Define the number of test records and output file path
    num_records = 100
    output_file = 'test_data.json'
    
    # Generate and save test data
    generate_test_data(num_records, output_file)
    
if __name__ == '__main__':
    main()