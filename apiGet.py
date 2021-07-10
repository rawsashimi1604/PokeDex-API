import requests

BASE = "http://127.0.0.1:5000/"

id = 1
response = requests.get(BASE + "pokemon/" + str(id))
output = response.json()

print(output)
