#displays suggestion based on budgeted amount and spending in a category
def suggestions(budget):
	spending = budget.total_spending()
	dict_budget = budget.budget
	for key in dict_budget.keys():

		print("Category: " + key + " | Budgeted: $"+ str(dict_budget[key]) + " | Spent: $" + str(spending[key]))
		if dict_budget[key] > spending[key]:
			print("Suggestion: Next budget, reduce the amount you expect to spend on " + key + ". (Good)")
		elif dict_budget[key] == spending[key]:
			print("Suggestion: Perfect, you spent the amount you budgeted for on " + key + "! (Perfrect)")
		elif dict_budget[key] < spending[key]:
			print("Suggestion: Over budget, you spent more then you budgeted for on " + key + ". (Bad)")
		print("- - - - - - - - - - - - - - - - - -")


