# PokeDex-API
Using knowledge I have learnt from previous tutorial to create a simple PokeDex API.

## Introduction
Hey guys! This is a simple REST API I made for Pokemon Data. I recently learnt how to make REST APIs from TechWithTim's Youtube Channel and I thought it would be a good way to
practice what I have learnt. :blush:

## Installation
To install the API, simply use pip install for the requirements.txt file.
```python
  pip install -r requirements.txt # method 1
  pip3 install -r requirements.txt # method 2
```

Then, proceed to delete the database.db file. Also uncomment this line of code in apiBuild.py to create a new database. *(Line 87)*
```python
  db.create_all()
```

## Example Usage
Firstly, go to apiBuild.py and run it.
Then open cmd and run apiPut.py

*PUT allows us to populate data in our database using pokemon.csv*

```python
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

```

To receive data from API, use a GET Request.
Open cmd and run apiGet.py

```python
import requests

BASE = "http://127.0.0.1:5000/"

id = 2
response = requests.get(BASE + "pokemon/" + str(id))
output = response.json()
```

Example Output:
```
  {'id': 2, 'name': 'Ivysaur', 'type1': 'Grass', 'type2': 'Poison', 'total': 405, 'hp': 60, 'attack': 62, 'defense': 63, 'sp_att': 80, 'sp_def': 80, 'speed': 60, 'generation': 1, 'legendary': 'False'}
``` 

You can also receive directly from the server. Simply open google chrome and navigate to the URL "http://127.0.0.1:5000/" after launching flask.
To get pokemon of ID : 2, use "http://127.0.0.1:5000/pokemon/2"

Example Output:
```json
{
    "id": 2,
    "name": "Ivysaur",
    "type1": "Grass",
    "type2": "Poison",
    "total": 405,
    "hp": 60,
    "attack": 62,
    "defense": 63,
    "sp_att": 80,
    "sp_def": 80,
    "speed": 60,
    "generation": 1,
    "legendary": "False"
}
```

