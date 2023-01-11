import requests

endpoint = 'http://127.0.0.1:8000/api/productdeleteapi/1'

# data = {'name' : 'Headphones1', 'description': 'All good', 'price' : 120}

response = requests.delete(endpoint)

print(response.status_code)