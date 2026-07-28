from abc import ABC, abstractmethod


class Animal(ABC):
	def __init__(self, name, habitat):
		self.name = name
		self.habitat = habitat

	def display_info(self):
		print(f"Animal Name: {self.name}")
		print(f"Habitat: {self.habitat}")

	@abstractmethod
	def sound(self):
		pass


class Dog(Animal):
	def __init__(self, name, habitat, breed):
		super().__init__(name, habitat)
		self.breed = breed

	def sound(self):
		print(f"{self.name} is a {self.breed} and says: Woof Woof!")


class Cat(Animal):
	def __init__(self, name, habitat, color):
		super().__init__(name, habitat)
		self.color = color

	def sound(self):
		print(f"{self.name} is a {self.color} cat and says: Meow Meow!")


animal_1 = Dog("Tommy", "Home", "Labrador")
animal_2 = Cat("Kitty", "House", "white")

print("===== Animal Class Demo =====")

animal_1.display_info()
animal_1.sound()

print()

animal_2.display_info()
animal_2.sound()
