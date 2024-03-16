import json

file_name = "data.json"

with open(file_name) as data:
    datos = json.load(data)

print(json.dumps(datos, indent=4))

