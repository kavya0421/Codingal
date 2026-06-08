# Dictionary of students
student_data = {
    "id1": {"name": "Sara"},
    "id2": {"name": "David"},
    "id3": {"name": "Sara"},
    "id4": {"name": "Surya"},
}

frequency = {}

# Count frequency of names
for student_id, details in student_data.items():
    name = details["name"]

    if name in frequency:
        frequency[name] += 1
    else:
        frequency[name] = 1

# Print output
for name, count in frequency.items():
    print(name, ":", count)