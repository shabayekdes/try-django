import requests


endpoint = "http://localhost:8000/api/products/" 

headers = {
    'Authorization': 'Bearer 0726edf7fb1efde89e5f8d158e2a26506762ca12'
}
data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())
