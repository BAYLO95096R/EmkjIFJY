# 代码生成时间: 2025-09-05 07:29:53
import json
def convert_json_format(input_data, output_format):
    """
    Converts JSON data to a specified format.

    Args:
        input_data (dict): The JSON data to be converted.
        output_format (str): The desired output format. Currently supports 'json', 'dict', 'list'.

    Returns:
        The input data in the specified output format.
    """
    try:
        if not isinstance(input_data, dict):
            raise ValueError("Input data must be a dictionary.")
        
        if output_format == 'json':
            # Convert to JSON string
            return json.dumps(input_data)
        elif output_format == 'dict':
            # JSON and dict are the same in Python, so just return the input
            return input_data
        elif output_format == 'list':
            # Assuming the input is a list of dictionaries
            if isinstance(input_data, list):
                return input_data
            else:
                raise ValueError("Input data must be a list when converting to 'list' format.")
        else:
            raise ValueError("Unsupported output format.")
    except ValueError as e:
        # Handle errors and print a user-friendly message
        print(f"Error: {e}")
        return None
def main():
    # Example usage
    example_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    print("Original JSON data:")
    print(convert_json_format(example_data, 'json'))  # Convert to JSON string
    print("
Converted to dictionary (no change): ")
    print(convert_json_format(example_data, 'dict'))  # Same as original
    print("
Converted to list (error): ")
    print(convert_json_format(example_data, 'list'))  # Should raise an error
    # Example with list of dictionaries
    example_list = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 24}
    ]
    print("
Converted list to list: ")
    print(convert_json_format(example_list, 'list'))  # Should work

if __name__ == "__main__":
    main()