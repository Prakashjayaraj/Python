import json

sampleJson = '''{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}'''

data = json.loads(sampleJson)
print(data['company']['employee']['payable']['bonus'])
