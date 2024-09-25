from expenses import Transaction
category_used = ["Food & Drink", "Entertainment", "Groceries", "Transport"]
class Budget:

	#budget = [{category: amount, ..}, [transaction]]
	def __init__(self, categories, amounts, transactions=[]):
		self._budget = {}
		for category in category_used:
			self._budget[category] = 0
		for i in range(len(categories)):
			if categories[i] in category_used:
				self._budget[categories[i]] = amounts[i]

		self._transactions = transactions

	#adds transactions to the budget
	def add_transaction(self, amount, date, name, category):
		newTransaction = Transaction(amount, date, name, category)
		self._transactions.append(newTransaction)
	
	#returns total amount spent in a category
	def total_spending_category(self, category):
		total = 0
		for expenses in self._transactions:
			if expenses.category == category:
				total += expenses.amount
		return total

	#displays transactions
	def print_transactions(self):
		for expense in self._transactions:
			print("Date: " + expense.date + ", Name: " + expense.name + ", Amount: " + expense.amount + ", Category: " + expense.category)
	
	#returns a dict of all of the spending in each category
	#{category: amount, ..}
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
	
	def to_dict(self):
		return {
			"budget": self._budget,
			"transactions": [transaction.to_dict() for transaction in self._transactions]
		}

	@classmethod
	def from_dict(cls, data):
		budget = cls(list(data["budget"].keys()), list(data["budget"].values()))
		budget._transactions = [Transaction.from_dict(t) for t in data["transactions"]]
		return budget

	def print_transactions(self):
		for transaction in self._transactions:
			print(f"Date: {transaction.date}, Name: {transaction.name}, Amount: {transaction.amount}, Category: {transaction.category}")

	def __repr__(self):
		return f"Budget({self._budget}, {len(self._transactions)} transactions)"

	
	