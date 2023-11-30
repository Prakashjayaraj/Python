import json

employee = {"name" :"prakash","age": 23, "location":"coimbatore"}
employee1 = {"name" :"ganesh","age": 22, "location":"pollachi"}
employee2 = {"name" :"varun","age": 32, "location":"banglore"}


Json_data = json.dumps(employee, indent=2 , separators=(",","="))
Json_data1 = json.dumps(employee1)
Json_data2= json.dumps(employee2)

print(Json_data,Json_data1,Json_data2)


