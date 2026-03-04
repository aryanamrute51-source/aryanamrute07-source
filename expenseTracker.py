 # EXPENSES TRACKER PROJECT       
    
expenseslist = [] # list of expenses in the form of dictonary
print("Welcome to expense tracker => ")

while True:
    print("\n### MENU ###")
    
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Cost")
    print("4. Exit")
    
    choice = int(input("Please enter your choice: "))
    
    
    # 1. Add expense
    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter the category (Food, Travel, Makeup, Books): ")
        description = input("Enter a short description: ")
        amount = float(input("Enter the amount: "))
        
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        expenseslist.append(expense)
        print("\nExpense added successfully!")
    
    # 2. View all expenses
    elif choice == 2:
        if len(expenseslist) == 0:
            print("No expenses added yet.")
        else:
            print("\n====== Your Expenses ======")
            count = 1
            for eachexpense in expenseslist:
                print(f"Expense {count} -> {eachexpense['date']}, {eachexpense['category']}, {eachexpense['description']}, {eachexpense['amount']}")
                count += 1
    
    
    # 3. View total spending
    elif choice == 3:
        # total = 0
        # for eachexpense in expenseslist:
        #     total = total+1
        total = sum(e['amount'] for e in expenseslist)
        print("\nTotal Spending:", total)
    
    
    # 4. Exit
    elif choice == 4:
        print("Exiting... Goodbye!")
        break
    
    else: 
        print("Invalid choice, please try again.") 