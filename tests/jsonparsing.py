import json
data = {
'item1': {
    'name': "A",
    'price': 10
    },
'item2': {
    'name': "B",
    'price': 20
    }
}


value = json.dumps(list(data.values()))
print(list(data.values()))