class Vehicle:

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

class Bus(Vehicle):

    def total_fare(self):
        return self.fare + (self.fare * 10 / 100)

School_bus = Bus("School Volvo", 500)

print("Vehicle Name:", School_bus.name)
print("Bus Fare:", School_bus.total_fare())