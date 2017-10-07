import json

j1 = '{"ip": "8.8.8.8"}'
d1 = json.loads(j1)

print(d1)
print(type(d1))
print(d1['ip'])