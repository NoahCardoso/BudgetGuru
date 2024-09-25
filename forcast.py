import numpy as np
from sklearn.linear_model import LinearRegression

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


def plot(sequence):

	# Prepare the data
	X = np.array([0, 1, 2]).reshape(-1, 1)  # Indices
	y = np.array(sequence)  # Sequence values
	print(sequence)
	# Create the model
	model = LinearRegression()

	# Train the model

	model.fit(X, y)

	# Predict the next number in the sequence
	next_index = np.array([[3]])
	predicted_value = model.predict(next_index)
	prediction = round(predicted_value[0],2)

	return prediction