class LibraryManagementSystem:
	def __init__(self, library_name):
		self.library_name = library_name
		self.books = []
		self.issued_books = []

		print(f"Welcome to {self.library_name}")
		print("Library management system is ready.")

	def add_book(self, book_name):
		self.books.append(book_name)
		print(f"'{book_name}' has been added to the library.")

	def remove_book(self, book_name):
		if book_name in self.books:
			self.books.remove(book_name)
			print(f"'{book_name}' has been removed from the library.")
		else:
			print(f"'{book_name}' was not found in the library.")

	def display_books(self):
		print(f"\n--- {self.library_name} Book List ---")
		if self.books:
			for number, book in enumerate(self.books, 1):
				status = "Issued" if book in self.issued_books else "Available"
				print(f"{number}. {book} - {status}")
		else:
			print("No books are available in the library.")

	def search_book(self, book_name):
		if book_name in self.books:
			print(f"'{book_name}' is available in the library.")
		else:
			print(f"'{book_name}' is not available in the library.")

	def issue_book(self, book_name):
		if book_name in self.books and book_name not in self.issued_books:
			self.issued_books.append(book_name)
			print(f"'{book_name}' has been issued.")
		elif book_name in self.issued_books:
			print(f"'{book_name}' is already issued.")
		else:
			print(f"'{book_name}' is not available in the library.")

	def return_book(self, book_name):
		if book_name in self.issued_books:
			self.issued_books.remove(book_name)
			print(f"'{book_name}' has been returned.")
		else:
			print(f"'{book_name}' was not issued.")


library = LibraryManagementSystem("City Central Library")

while True:
	print("\n========= LIBRARY MENU =========")
	print("1. Add Book")
	print("2. Remove Book")
	print("3. Display Books")
	print("4. Search Book")
	print("5. Issue Book")
	print("6. Return Book")
	print("7. Exit")
	print("===============================")

	choice = input("Enter your choice: ")

	if choice == "1":
		book_name = input("Enter the book name to add: ")
		library.add_book(book_name)

	elif choice == "2":
		book_name = input("Enter the book name to remove: ")
		library.remove_book(book_name)

	elif choice == "3":
		library.display_books()

	elif choice == "4":
		book_name = input("Enter the book name to search: ")
		library.search_book(book_name)

	elif choice == "5":
		book_name = input("Enter the book name to issue: ")
		library.issue_book(book_name)

	elif choice == "6":
		book_name = input("Enter the book name to return: ")
		library.return_book(book_name)

	elif choice == "7":
		print("Exiting the Library Management System.")
		break

	else:
		print("Invalid choice. Please enter a number from 1 to 7.")
