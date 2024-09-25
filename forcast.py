
def predict_spending(budget, category):
	total_transactions = []

	for transaction in budget.transactions:
		if transaction.category == category:
			total_transactions.append(transaction.amount)

	return plot(total_transactions)

def forcast_spending(all_budgets, category):
	if len(all_budgets) > 1:
		total_transactions = []
		for budget in all_budgets:
			temp_transactions = []
			for transaction in budget.transactions:
				if transaction.category == category:
					temp_transactions.append(transaction.amount)
			total_transactions.append(sum(temp_transactions))
		return plot(total_transactions)
	else:
		print("More budgets are needed to predict next months spending")
		return 0

def forcast_spending_next_budget(all_budgets, categories):
	my_dict = {}
	for category in categories:
		my_dict[category] = forcast_spending(all_budgets, category)
	return my_dict


def predict_spending_next_budget(budget, categories):
	my_dict = {}
	for category in categories:
		my_dict[category] = predict_spending(budget, category)
	return my_dict


def plot(y):
	x = []
	n = len(y)
	for i in range(n):
		x.append(i+1)
	sum_x = sum(x)
	sum_y = sum(y)
	sum_xy = 0
	for i in range(n):
		sum_xy += x[i] * y[i]
	sum_x2 = sum(i ** 2 for i in x)
	m = 0
	try:
		# Slope of the best line of fit
		m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
	except ZeroDivisionError:
		return 0
	# Intercept of the best line of fit
	b = (sum_y - m * sum_x) / n
	# Predict the next point on the line of best fit
	predict = m * (n + 1) + b
	return predict