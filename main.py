import json
import os
from budget import Budget
from forcast import forcast_spending_next_budget, predict_spending_next_budget
from graphme import make_report
from suggestions import suggestions
from expenses import Transaction

SAVE_FILE = "budgets_data.json"
categories = ["Food & Drink", "Entertainment", "Groceries", "Transport"]


def save_data(current_budget, budgets):
    data = {
        "current_budget": current_budget.to_dict(),
        "budgets": [budget.to_dict() for budget in budgets]
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("Data saved successfully.")


def load_data():
    if not os.path.exists(SAVE_FILE):
        return None, []

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    budgets = [Budget.from_dict(b) for b in data["budgets"]]
    current_budget = Budget.from_dict(data["current_budget"])
    return current_budget, budgets


def end_line():
    print("\n" + "- " * 10 + "\n")


def do_while_int(a, b):
    n = a
    while not (n > a and n < b):
        try:
            n = int(input())
        except ValueError:
            n = a
            print("Error: Must be an int")
    return n


def main():
    # Load existing data if available
    current_budget, budgets = load_data()

    if not budgets:  # Initialize if no data exists
        budgets = [Budget(categories, [0, 0, 0, 0], [Transaction(10, "", "", "Transport"),]),Budget(categories, [0, 0, 0, 0], [Transaction(10, "", "", "Transport"),])]
        current_budget = Budget(categories, [0, 0, 0, 0], [Transaction(10, "", "", "Transport"),])

    while True:
        print("1. Budget")
        print("2. Transaction")
        print("3. View Report")
        print("4. View Suggestions")
        print("5. View Predictions")
        print("Press 'q' to exit")

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
                        amounts = [int(amount) for amount in amounts]
                        budgets.append(Budget(categories, amounts))
                        current_budget = budgets[-1]
                        print(current_budget)
                        
                    except (IndexError, ValueError):
                        print("Error! Please enter valid numbers!")

                elif choice == "2":
                    for i, budget in enumerate(budgets, 1):
                        print(f"{i}. {budget}")
                    try:
                        index = int(input("Select a budget by number: "))
                        if 1 <= index <= len(budgets):
                            current_budget = budgets[index - 1]
                            print("Done")
                        else:
                            print("Error! Budget not found!")
                    except ValueError:
                        print("Error! You must enter a number!")

                elif choice == "3":
                    print(current_budget) 

                elif choice == "q":
                    break
                end_line()

        # Transaction handling
        elif choice == "2":
            end_line()
            while True:
                print("1. Add Transaction")
                print("2. View Transactions")
                choice = input()

                if choice == "1":
                    end_line()
                    print("How many transactions would you like to add?")
                    n = do_while_int(0, 100)
                    print("Amount | Date | Name | Category")
                    for i in range(n):
                        while True:
                            try:
                                amount, date, name, category = input().split(" ")
                                amount = int(amount)
                                current_budget.add_transaction(amount, date, name, category)
                                if category in categories:
                                    break
                            except ValueError:
                                print("Error! Enter valid values.")

                elif choice == "2":
                    current_budget.print_transactions()

                elif choice == "q":
                    break
                end_line()

        # Report
        elif choice == "3":
            end_line()
            print("View Budget vs Spending")
            make_report(current_budget.budget, current_budget.total_spending())
            print("Red show spending. Green shows you budgeted amount")
            input()

        #feedback on budget
        elif choice == "4":
            end_line()
            suggestions(current_budget)
            choice = input("press q")

        #forcast future spending
        elif choice == "5":
            while True:
                end_line()
                print("1. Predict based on previous budgets (Requires minimum of 2 budgets)")
                print("2. Predict based current budget")
                choice = input()
                if choice == "1":
                    make_report(current_budget.budget,
                                forcast_spending_next_budget(budgets, categories))
                elif choice == "2":
                    make_report(current_budget.budget, predict_spending_next_budget(
                        current_budget, categories))
                elif choice == "q":
                    break
                end_line()

        elif choice == "q":
			# Save data before exiting
           save_data(current_budget, budgets)
           break
        end_line()

if __name__ == "__main__":
    main()
