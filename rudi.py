import json

file = open('tes.json')

data = json.loads(file.read())

print(data)