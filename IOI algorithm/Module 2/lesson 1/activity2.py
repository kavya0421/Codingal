print("==============================")
print("DICTIONARY OPERATIONS")
print("==============================")

student = {
	"name": "Aarav",
	"age": 12,
	"class": "6A",
	"city": "Pune"
}

print("Original Dictionary:", student)
print("Name:", student["name"])
print("Age:", student.get("age"))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student["age"] = 13
student["school"] = "Green Valley School"
print("\nAfter Update and Add:", student)

removed_city = student.pop("city")
print("Removed City:", removed_city)
print("After Removing City:", student)

student_copy = student.copy()
print("Copied Dictionary:", student_copy)
