import requests

response = requests.get('http://127.0.0.1:8000/drinks')
data = response.json()

for i in data:
    print('ID: ', i['id'])
    print('Name: ', i['name'])
    print('Description: ', i['description'])