import requests

BASE = "http://127.0.0.1:5000/"
id = 1

data = {"hp": 500}  # Example of HP Patch ==> 500 hp.
response = requests.patch(BASE + f"pokemon/{id}", data)
output = response.json()
