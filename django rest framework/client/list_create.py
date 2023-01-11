import requests

endpoint = 'http://127.0.0.1:8000/api/productlistcreateapi/' # to get details of product pass its id at last

# json={'name' : 'Shoes', 'description': 'All good', 'price' : "ABS"}
data = requests.get(endpoint)

print(data.text)