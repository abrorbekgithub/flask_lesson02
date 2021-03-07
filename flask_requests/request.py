import requests

data=requests.get('http://localhost:5000/api')
print(data.json())