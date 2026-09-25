def reverse_array(array):
	left = 0
	right = len(array) - 1

	while left < right:
		array[left], array[right] = array[right], array[left]
		left += 1
		right -= 1


numbers = [6, 5, 4, 3, 2, 1]

print("Original array : ", numbers)
reverse_array(numbers)
print("Reversed array : ", numbers)
