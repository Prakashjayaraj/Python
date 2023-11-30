class vechicle:

    def __init__(self, mileage, max_speed):
        self.mileage = mileage
        self.max_speed = max_speed


class car(vechicle):
    pass

car1 = car(12,133)

print(isinstance(car1,vechicle))