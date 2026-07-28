print("==============================")
print("SET OPERATIONS")
print("==============================")

fruits_a = {"apple", "banana", "orange", "grapes"}
fruits_b = {"banana", "kiwi", "orange", "mango"}

print("Set A:", fruits_a)
print("Set B:", fruits_b)

print("\nUnion:", fruits_a.union(fruits_b))
print("Intersection:", fruits_a.intersection(fruits_b))
print("Difference A - B:", fruits_a.difference(fruits_b))
print("Difference B - A:", fruits_b.difference(fruits_a))
print("Symmetric Difference:", fruits_a.symmetric_difference(fruits_b))

fruits_a.add("pear")
fruits_b.discard("mango")

print("\nAfter Add and Remove:")
print("Set A:", fruits_a)
print("Set B:", fruits_b)
