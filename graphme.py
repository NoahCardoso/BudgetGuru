import matplotlib.pyplot as plt

def make_report(budget, spending):
	# Sample data
	categories = list(budget.keys())
	spent = list(spending.values())
	budgets = list(budget.values())


	# Set the positions for the bars
	bar_width = 0.35
	index = range(len(categories))

	# Create side-by-side bar charts
	plt.bar(index, spent, bar_width, color='red', label='Spent')
	plt.bar([i + bar_width for i in index], budgets, bar_width, color='green', label='Budget')

	# Add labels and title
	plt.xlabel('Categories')
	plt.ylabel('Amount ($)')
	plt.title('Budget vs Spending')
	plt.xticks([i + bar_width / 2 for i in index], categories)

	# Save the plot as a PNG file
	plt.savefig('budget_vs_spending.png')
	print("done")
	# Alternatively, you can use other formats like:
	# plt.savefig('budget_vs_spending.jpg')
