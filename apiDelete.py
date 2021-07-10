import requests

BASE = "http://127.0.0.1:5000/"

id = 2
response = requests.delete(BASE + f"pokemon/{id}")
output = response.json()

print(output)
