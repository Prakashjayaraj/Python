class vechicle:
    color = "white"
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vechicle):
    pass
class car(vechicle):
    pass

vechile = bus("polo",156,31)
print(vechile.name,vechile.mileage,vechile.max_speed, vechile.color)

vechile1 = car("audi a7",231,20)
print(vechile1.name,vechile1.mileage,vechile1.max_speed, vechile.color)
