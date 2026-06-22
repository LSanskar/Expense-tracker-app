    # expenses = []
    # while (True):
    #     add_expense = input("Do you wanna add an expense(Y/N)")
    #     if (add_expense=="Y"):
    #         expense_definition = input("Enter what the expense is: ")
    #         expense_cost = int(input("Enter the cost of the expense"))
    #         expenses.append({expense_definition:expense_cost})
    #         print(expenses)
    #     elif (add_expense=="N" or add_expense=="n"):
    #         break
    #     else:
    #         print("enter a valid response")

import shelve
categories = ['Groceries', 'Bills', 'Rent', 'Miscellaneous']  
        

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Add custom categories")
    print("4. Total spending")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        with shelve.open('expenses_data') as db:
            if ('expenses' in db):
                temp_expenses = db["expenses"]
            else:
                temp_expenses = []       
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        for i in categories:
            print(i)
        category = input("Choose between the categories for this expense")    
        while (not(category in categories)):
            print("Enter valid response")
            category = input("Choose between the categories for this expense")
        else:
            temp_expenses.append((name,amount,category))
        with shelve.open('expenses_data') as db:
            db["expenses"]= temp_expenses
            print(temp_expenses)
        
            
            
    elif choice == "2":
        with shelve.open('expenses_data') as db:
            data = db["expenses"]
        for i in data:
            print(i)    

    elif choice== "3":
        new_category = input("add new category: ")
        categories.append(new_category)
    

    elif choice== "4":
        total=0
        with shelve.open('expenses_data') as db:
            expenses = db['expenses']
            for expense in expenses:
                total+=expense[1]
        print(total)    

    elif choice == "5":
        break        

