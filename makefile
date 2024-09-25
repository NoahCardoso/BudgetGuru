PYTHON=python3
PIP=pip3
#BudgetGuru
install:
	$(PIP) install -r requirements.txt
run:
	$(PYTHON) main.py