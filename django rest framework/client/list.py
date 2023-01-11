import requests

# endpointf = 'http://127.0.0.1:8000/api/productlistapif/' 
# endpointc = 'http://127.0.0.1:8000/api/productlistapi/'

endpoint = 'http://127.0.0.1:8000/api/viewset/products/'

# json={'name' : 'Shoes', 'description': 'All good', 'price' : "ABS"}
# dataf = requests.get(endpointf)
data = requests.get(endpoint)


print(data.text)

