class BankAccount:
	def __init__(self, account_holder, balance):
		self.account_holder = account_holder
		self.__balance = balance

	def get_balance(self):
		return self.__balance

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			print(f"{amount} deposited successfully.")
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):
		if amount > 0 and amount <= self.__balance:
			self.__balance -= amount
			print(f"{amount} withdrawn successfully.")
		else:
			print("Invalid withdrawal amount.")

	def display_account(self):
		print(f"Account Holder: {self.account_holder}")
		print(f"Balance: {self.__balance}")


account = BankAccount("Aarav", 5000)

print("===== Encapsulation Demo =====")
account.display_account()

print("\nDepositing Money")
account.deposit(1500)
print("Current Balance:", account.get_balance())

print("\nWithdrawing Money")
account.withdraw(2000)
print("Current Balance:", account.get_balance())

print("\nFinal Account Details")
account.display_account()
