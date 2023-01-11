import requests

endpointf = 'http://127.0.0.1:8000/api/productdetailapif/1/' 
endpointc = 'http://127.0.0.1:8000/api/productdetailapi/1/'

# json={'name' : 'Shoes', 'description': 'All good', 'price' : "ABS"}
dataf = requests.get(endpointf)
datac = requests.get(endpointc)

print("Funtion view ->")
print(dataf.text)

print("Class view ->")
print(datac.text)
