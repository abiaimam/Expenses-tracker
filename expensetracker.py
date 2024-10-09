expenses = {}

# add expense
def add_expense(date, amount, description):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({"amount": amount, "description": description})
    print(f"Added expense: ${amount} for '{description}' on {date}")

# view expenses
def view_expenses():
    if not expenses:
        print("No expenses.")
    else:
        for date, expense_list in expenses.items():
            print(f"\nDate: {date}")
            for expense in expense_list:
                print(f" - Amount: ${expense['amount']}, Description: {expense['description']}")

# deleting expense
def delete_expense(date, description):
    if date in expenses:
        for i, expense in enumerate(expenses[date]):
            if expense['description'] == description:
                del expenses[date][i]
                print(f"Deleted expense '{description}' on {date}")
                if not expenses[date]:  
                    del expenses[date]
                return
        print(f"Expense with description '{description}' not found on {date}")
    else:
        print(f"No expenses found on {date}")

# Calculate total expenses
def calculate_total():
    total = sum(expense['amount'] for expense_list in expenses.values() for expense in expense_list)
    print(f"Total expenses: ${total}")

while True:
    print("\nWelcome to the Expense Tracker")
    print("Select an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Calculate Total Expense")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        date = input("Enter the date (MM-DD-YYYY): ")
        amount = float(input("Enter the amount: $"))
        description = input("Enter the description: ")
        add_expense(date, amount, description)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        date = input("Enter the date (MM-DD-YYYY): ")
        description = input("Enter the description: ")
        delete_expense(date, description)
    elif choice == '4':
        calculate_total()
    elif choice == '5':
        print("Exiting the expense tracker.")
        break
    else:
        print("Invalid, please choose again.")

