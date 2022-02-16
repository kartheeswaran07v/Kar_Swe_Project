import requests

response = requests.get("https://api.npoint.io/f45b3e0d75b04a3b21c7")

data = response.json()
print(data)