import requests

endpoint = 'http://127.0.0.1:8000/api/productupdateapi/1'

data = {'name' : 'Headphones1', 'description': 'All good', 'price' : 120}

response = requests.put(endpoint, json=data)

print(response.text)