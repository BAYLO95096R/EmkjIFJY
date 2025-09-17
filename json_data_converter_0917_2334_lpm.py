# 代码生成时间: 2025-09-17 23:34:09
import json
def convert_json_to_python(data):
    """
    Converts JSON data to a Python object.

    Args:
        data (str): A string containing JSON data.

    Returns:
        object: The Python object corresponding to the JSON data.
    """
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON data: {e}")
def convert_python_to_json(obj):
    """
    Converts a Python object to a JSON string.

    Args:
        obj (object): The Python object to be converted.

    Returns:
        str: A JSON string representing the Python object.
    """
    try:
        return json.dumps(obj, indent=4)
    except (TypeError, OverflowError) as e:
        raise ValueError(f"Cannot convert object to JSON: {e}")
def main():
    # Example usage
    json_str = "{"name": "John", "age": 30}"
    try:
        python_obj = convert_json_to_python(json_str)
        print("Python Object: ", python_obj)
        json_str_converted = convert_python_to_json(python_obj)
        print("Converted JSON String: ", json_str_converted)
    except ValueError as e:
        print(e)if __name__ == "__main__":
    main()