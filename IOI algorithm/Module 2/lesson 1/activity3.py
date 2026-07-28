print("==============================")
print("LIST TO DICTIONARY")
print("==============================")

item_ids = [1, 2, 3, 4]
item_names = ["Pen", "Pencil", "Book", "Eraser"]

items = dict(zip(item_ids, item_names))

print("List of IDs:", item_ids)
print("List of Names:", item_names)
print("Converted Dictionary:", items)
