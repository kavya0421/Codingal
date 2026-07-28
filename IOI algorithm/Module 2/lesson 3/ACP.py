class Robot:
	def __init__(self, name):
		self.name = name

	def introduce(self):
		print("Hello, my name is", self.name)


tom = Robot("Tom")
jerry = Robot("Jerry")

print("Robot Introductions:")
tom.introduce()
jerry.introduce()
