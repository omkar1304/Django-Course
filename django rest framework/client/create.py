import requests

# endpointf = 'http://127.0.0.1:8000/api/productcreateapif/' 
# endpointc = 'http://127.0.0.1:8000/api/productcreateapi/'

endpoint = 'http://127.0.0.1:8000/api/viewset/products/'


data = {'name' : 'Frame', 'description': 'All good', 'price' : 100}

# dataf = requests.post(endpointf, json=data)
datac = requests.post(endpoint, json=data)

# print("Funtion view ->")
# print(dataf.text)

print("Class view ->")
print(datac.text)




