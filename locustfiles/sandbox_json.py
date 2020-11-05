import json

with open('.\detail.json') as f:
            data = json.load(f)
print(data)
print(data[0]['ImageSize'])