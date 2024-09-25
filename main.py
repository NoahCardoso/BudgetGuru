from budget import Budget
from expenses import Transaction
from forcast import forcast_spending_next_budget, predict_spending_next_budget
from graphme import make_report
from suggestions import suggestions


categories = ["Food & Drink", "Entertainment", "Groceries", "Transport"]
		
def end_line():
	print("")
	print("- " * 10)
	print("")
def do_while_int(a, b):
	n = a
	while not(n > a and n < b):
		try:
			n = int(input())
		except ValueError:
			n = a
			print("Error: Must be an int")
	return n


def main():

	budgets = [Budget(categories, [10, 10, 10, 10], []), Budget(categories, [20, 15, 30, 60], [Transaction(10, "n", "n", "Transport"), Transaction(20, "n", "n", "Transport")])]
	current_budget = budgets[-1]
	while True:
		print("1. Budget")
		print("2. Transaction")
		print("3. View Report")
		print("4. View Suggestions")
		print("5. View Predictions")
		print("press q to esc any menu")

		choice = input()

		if choice == "1":
			end_line()
			while True:
				
				print("1. Add Budget")
				print("2. Select Budget")
				print("3. View Budget")

				choice = input()
				end_line()
				if choice == "1":
					print("Enter amount for each category: 10 20 20 30")
					print(" ".join(categories))
					amounts = input().split(" ")

					try:
						for i in range(len(categories)):
							amounts[i] = int(amounts[i])

						budgets.append(Budget(categories, amounts))
						current_budget = budgets[-1]
						print(current_budget)
					except IndexError:
						print("Error! You must enter a positive number!")
					except ValueError:
						print("Error! You must enter a number!")
					
					print()

				elif choice == "2":
					end_line()
					for budget, i in zip(budgets, range(1, len(budgets)+1)):
						print(str(i) + ". ", end="")
						print(budget)
					try:
						index = int(input())
						if index > 0 and index <= len(budgets):
							current_budget = budgets[index-1]
							print("Done")
						else:
							print("Error! Budget not found!")
					except ValueError:
						print("Error! You must enter a number!")

					print()

				elif choice == "3":
					print(current_budget)

				elif choice == "q":
					break
		

		# Transcations
		elif choice == "2":
			end_line()
			while True:
				print("1. Add Transaction")
				print("2. View Transactions")
				choice = input()

				if choice == "1":
					end_line()

					print("How many transactions would you like to add?")

					n = do_while_int(0,100)

					print()
					print("Amount | Date | Name | Category")
					for i in range(n):
						amount, data, name, category = [-1, "", "", ""]
						while not (amount >= 0):
							amount, data, name, category = input().split(" ")
							try:
								amount = int(amount)
							except ValueError:
								print("Error! Amount must be an int!")
						current_budget.add_transaction(amount, data, name, category)

				elif choice == "2":
					end_line()
					current_budget.print_transactions()
				elif choice == "q":
					break

		# Report
		elif choice == "3":
			end_line()
			print("View Budget vs Spending")
			make_report(current_budget.budget, current_budget.total_spending())
			print("Red show spending. Green shows you budgeted amount")
			input()
		
		elif choice == "4":
			end_line()
			suggestions(current_budget)
			choice = input("press q")
			break

		elif choice == "5":
			end_line()
			print("1. Predict based on previous budgets")
			print("2. Predict based current budget")
			choice = input()
			if choice == "1":
				make_report(current_budget.budget, forcast_spending_next_budget(budgets, categories))
			elif choice == "2":
				make_report(current_budget.budget, predict_spending_next_budget(current_budget, categories))
			temp = input()
			

		end_line()
	
	


main()

'''
		elif choice == 2:
			print(budget.total_spending())
			make_report(budget.budget, budget.total_spending())
			break
		elif choice == 3:
			suggestions(budget)
		elif choice == 5:
			print(predict_spending_next_budget(all_budgets, categories))
			make_report(budget2.budget, predict_spending_next_budget(all_budgets, categories))
		elif choice == 6:
			print(predict_spending(all_budgets, "Food & Drink"))
		'''