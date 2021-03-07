import requests

data=requests.get('http://127.0.0.1:5000/api?a=5&b=8')
print(data.json())