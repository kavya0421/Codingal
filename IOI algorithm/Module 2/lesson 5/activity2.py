from abc import ABC, abstractmethod


class Student(ABC):
	def __init__(self, name, roll_no, student_class):
		self.name = name
		self.roll_no = roll_no
		self.student_class = student_class

	def display_details(self):
		print(f"Student Name: {self.name}")
		print(f"Roll Number: {self.roll_no}")
		print(f"Class: {self.student_class}")

	@abstractmethod
	def show_result(self):
		pass


class SchoolStudent(Student):
	def __init__(self, name, roll_no, student_class, marks):
		super().__init__(name, roll_no, student_class)
		self.marks = marks

	def show_result(self):
		total = sum(self.marks)
		percentage = total / len(self.marks)

		if percentage >= 90:
			grade = "A+"
		elif percentage >= 75:
			grade = "A"
		elif percentage >= 60:
			grade = "B"
		else:
			grade = "C"

		print(f"Marks: {self.marks}")
		print(f"Percentage: {percentage:.2f}%")
		print(f"Grade: {grade}")


student_1 = SchoolStudent("Aarav", 12, "6A", [92, 88, 95, 90, 87])

print("===== Student Details =====")
student_1.display_details()
student_1.show_result()
