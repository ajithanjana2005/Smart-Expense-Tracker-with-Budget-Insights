
expenses = []  


total_budget = float(input("Enter your budget in INR: "))


while True:
    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. View Budget Status")
    print("3. Show Expense Report")
    print("4. Exit")

  
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        
        category = input("Enter expense category (e.g., Food, Travel): ")
        amount = float(input("Enter amount in INR: "))
        expenses.append((category, amount))  
        print(f"Added: {category} - ₹{amount}")

    elif choice == "2":
        
        total_spent = sum(e[1] for e in expenses)
        remaining_budget = total_budget - total_spent
        print(f"Total Spent: ₹{total_spent}")
        print(f"Remaining Budget: ₹{remaining_budget}")

    elif choice == "3":
       
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nExpense Report:")
            report = {}
            for category, amount in expenses:
                report[category] = report.get(category, 0) + amount
            for category, total in report.items():
                print(f"{category}: ₹{total}")

    elif choice == "4":
       
        print("Exiting the program. ")
        break

    else:
       
        print("Invalid choice. Please enter a number between 1 and 4.")
