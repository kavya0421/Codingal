# import necessary packages
from abc import ABC, abstractmethod

# create a base class
class Vehicle(ABC):

    # abstract method
    def move(self):
        pass

# sub classes
class Car(Vehicle):

    def move(self):
        print("Car is driving")

class Bike(Vehicle):

    def move(self):
        print("Bike is riding")

class Bus(Vehicle):

    def move(self):
        print("Bus is transporting passengers")

class Train(Vehicle):

    def move(self):
        print("Train is running on tracks")

# Driver code
v1 = Car()
v1.move()

v2 = Bike()
v2.move()

v3 = Bus()
v3.move()

v4 = Train()
v4.move()