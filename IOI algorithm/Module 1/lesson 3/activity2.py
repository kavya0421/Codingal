print("==============================")
print("BMI CALCULATOR")
print("==============================")

name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if height <= 0:
	print("Height must be greater than 0.")
else:
	bmi = weight / (height * height)

	if bmi < 18.5:
		category = "Underweight"
	elif bmi < 25:
		category = "Normal weight"
	elif bmi < 30:
		category = "Overweight"
	else:
		category = "Obese"

	print("\n================================")
	print("BMI REPORT")
	print("================================")
	print("Name:", name)
	print("Weight:", weight, "kg")
	print("Height:", height, "m")
	print("BMI:", round(bmi, 2))
	print("Category:", category)
