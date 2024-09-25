class Transaction:
	#Transaction(amount, "date", "name", "category")
	def __init__(self, amount, date, name, category):
		self._amount = float(f"{(amount):.4f}")
		self._date = date
		self._name = name
		self._category = category

	@property
	def amount(self):
		return self._amount
	
	@amount.setter
	def amount(self, value):
		if not isinstance(value, str):
			raise ValueError("Amount must be a number")
		self._amount = value
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		if not isinstance(value, str):
			raise ValueError("Name must be a string")
		self._name = value

	@property
	def date(self):
		return self._date
	
	@date.setter
	def date(self, value):
		if not isinstance(value, str):
			raise ValueError("Date must be a string")
		self._date = value
	
	@property
	def category(self):
		return self._category
	
	@category.setter
	def category(self, value):
		if not isinstance(value, str):
			raise ValueError("Category must be a string")
		self._category = value
	
	def to_dict(self):
		return {
			"amount": self.amount,
			"date": self.date,
			"name": self.name,
			"category": self.category
		}

	@classmethod
	def from_dict(cls, data):
		return cls(data["amount"], data["date"], data["name"], data["category"])

	def __repr__(self):
		return f"Transaction({self.amount}, {self.date}, {self.name}, {self.category})"
		
	


