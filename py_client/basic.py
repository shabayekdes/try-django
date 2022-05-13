import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={'page': 1}, json={"product_id": 123 }) # HTTP Request
# print(get_response.headers)
# print(get_response.text) # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict

print(get_response.json())
