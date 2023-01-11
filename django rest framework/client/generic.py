import requests


'''to get list API ->'''
# endpoint = 'http://127.0.0.1:8000/api/productgenericapi/'
# response = requests.get(endpoint)
# print(response.text)


'''to get detail API ->'''
# endpoint = 'http://127.0.0.1:8000/api/productgenericapi/2'
# response = requests.get(endpoint)
# print(response.text)


'''to create API ->'''
# endpoint = 'http://127.0.0.1:8000/api/productgenericapi/'
# data = {'name' : 'Frame', 'description': 'All good', 'price' : 100}
# response = requests.post(endpoint, json=data)
# print(response.text)


'''to update API ->'''
# endpoint = 'http://127.0.0.1:8000/api/productgenericapi/2'
# data = {'name' : 'updated', 'description': 'All good', 'price' : 1111}
# response = requests.put(endpoint, json=data)
# print(response.text)

'''to delete API ->'''
# endpoint = 'http://127.0.0.1:8000/api/productgenericapi/2'
# response = requests.delete(endpoint)
# print(response.status_code)


'''to build token and handle token based authentication ->'''
from getpass import getpass

# get the token from authtoken views
auth_endpoint = 'http://127.0.0.1:8000/api/auth/'

# provide username and password
username =  input("Enter your username \n")
password = getpass("Enter your password \n")

# as it is post request. hence pass json data with username and password and get the token
auth_response = requests.post(auth_endpoint, json={'username' : username, 'password' : password})

# if we get the token i.e. code => 200 then build headers 
# and pass with URL which need tokenbased authentication
if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization" : f"Token {token}"
    }
    endpoint = 'http://127.0.0.1:8000/api/productgenericapi/'
    response = requests.get(endpoint, headers=headers)
    print(response.text)
else:
    print("Invalid token")


