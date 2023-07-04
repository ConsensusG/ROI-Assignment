class ROI_calc():

    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def my_cash_flow(self):
        cash_flow = int(self.income) - int(self.expenses)
        return cash_flow


def calculate():
    while True:
        print("What would you like to do?")
        print("1. Enter my income and expenses.")
        print("2. Calculate my cash flow.")
        print("3. Exit the program,")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            income = input("Enter your monthly income: ")
            expenses = input("Now enter your expenses: ")
            roi = ROI_calc(income, expenses)

        if choice == "2":
            cash_flow = roi.my_cash_flow()
            print(f"Your cash flow is: {cash_flow}")

        if choice == "3":
            break

calculate()