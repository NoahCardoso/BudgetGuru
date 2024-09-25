from expenses import Transaction
category_used = ["Food & Drink", "Entertainment", "Groceries", "Transport"]
class Budget:

	def __init__(self, categories, amounts, transactions=[]):
		self._budget = {}
		for category in category_used:
			self._budget[category] = 0
		for i in range(len(categories)):
			if categories[i] in category_used:
				self._budget[categories[i]] = amounts[i]

		self._transactions = transactions

	def add_transaction(self, amount, date, name, category):
		newTransaction = Transaction(amount, date, name, category)
		self._transactions.append(Transaction)
	
	def total_expenses_of(self, category):
		total = 0
		for expenses in self._transactions:
			if expenses.category == category:
				total += expenses.amount
		return total

	def print_transactions(self):
		for expense in self._transactions:
			print("Date: " + expense.date + ", Name: " + expense.name + ", Amount: " + expense.amount + ", Category: " + expense.category)
	
	def total_spending(self):
		my_dict = {}
		for category in category_used:
			my_dict[category] = 0
		for transaction in self._transactions:
			my_dict[transaction.category] = transaction.amount
		return my_dict
	
	@property
	def transactions(self):
		return self._transactions
	
	@property
	def budget(self):
		return self._budget
	
	def __repr__(self):
		transactions_str = " | ".join([str(transaction) for transaction in self._transactions])
		return f"Budget\t\t | {self._budget}\nTransactions\t | {transactions_str}\n"
	
	