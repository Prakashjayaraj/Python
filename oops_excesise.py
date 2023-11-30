class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self, capacity):
        print(f"The seating capacity is {capacity}")

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        super().seating_capacity(capacity)

vehicle = Vehicle("Pulsar", 222, 40)
print(vehicle.name, vehicle.max_speed, vehicle.mileage)
vehicle.seating_capacity(40)  # Calling the method with default capacity
