import csv
import requests
import time


def format(data: dict):
    formatInt = ['total', 'hp', 'attack',
                 'defense', 'sp_att', 'sp_def', 'speed', 'generation']

    for key in data:
        if key in formatInt:
            data[key] = int(data[key])
    return data


BASE = "http://127.0.0.1:5000/"  # Server API is running on.

reader = csv.DictReader(open("pokemon.csv"))

data = []
counter = 0
for row in reader:
    data.append(format(row))
    counter += 1

for i in range(1, counter + 1):
    response = requests.put(BASE + f"pokemon/{i}", data[i-1])
    print(response.json())
    time.sleep(0.1)
