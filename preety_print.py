import json

sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
prettyPrint  = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrint)
