import  json
import json

employee = '{"name": "prakash", "age": 23, "location": "coimbatore"}'
employee1 = '{"name": "varun", "age": 24, "location": "noida"}'

load = json.loads(employee)
print(load['age'])
# load a locartion in employee1
load1= json.loads(employee1)
print(load1['location'])

