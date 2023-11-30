import json

sampleJson = """[ 
   { 
      "id": 1,
      "name": "prakash",
      "location": {
         "permanent": "pollachi",
         "resident": "coimbatore"
      }
   },
   { 
      "id": 2,
      "name": "ganesh",
      "location": {
         "permanent": "pollachi",
         "resident": "coimbatore"
      }
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as exception:
    print(exception)
#grt the values
dataList = [item.get('id') for item in data]
print(dataList)
