# 代码生成时间: 2025-09-04 16:07:01
import json
from scrapy.http import Response

def format_api_response(response: Response) -> str:
    """
    Formats the API response from a Scrapy Response object into a JSON string.
    
    :param response: A Scrapy Response object
    :return: A formatted JSON string representing the API response
    """
    if not isinstance(response, Response):
        raise TypeError("Expected a Scrapy Response object")
    
    try:
        data = response.json()  # Parse the JSON response
        formatted_data = json.dumps(data, indent=4)  # Format the JSON data with indentation for readability
        return formatted_data
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response")
    except Exception as e:
        raise e

def main():
    # Example usage of the format_api_response function
    # Note: The actual Scrapy Response object would be obtained from a Scrapy Spider
    example_response = Response(
        url="http://example.com/api",
        status=200,
        headers={"Content-Type": "application/json"},
        body='{"key": "value"}'
    )
    try:
        formatted_response = format_api_response(example_response)
        print(formatted_response)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()