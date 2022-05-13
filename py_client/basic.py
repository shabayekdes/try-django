import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={'page': 1}, json={"product_id": 123 }) # HTTP Request
# print raw text response
# print(get_response.text) 

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
# print(get_response.json())
print(get_response.status_code)

print(get_response.json())
