import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, model, speed, mileage):
        self.model = model
        self.speed = speed
        self.mileage = mileage

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vec = Vehicle("honda", "123", "33")
json_file = json.dumps(vec, indent=4, cls=VehicleEncoder)
print(json_file)
