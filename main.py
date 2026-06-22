import shelve
categories = {1:'Groceries'
              ,2: 'Bills'
              ,3: 'Rent'
              ,4: 'Miscellaneous'}  
        

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
            print(f"{i}:{categories[i]}")
        category_selector = int(input("Choose between the categories for this expense"))    
        while (not(category_selector in categories)):
            print("Enter valid response")
            category_selector = input("Choose between the categories for this expense")
        else:
            temp_expenses.append((name,amount,categories[category_selector]))
        with shelve.open('expenses_data') as db:
            db["expenses"]= temp_expenses
            print(temp_expenses)
        
            
            
    elif choice == "2":
        with shelve.open('expenses_data') as db:
            if ('expenses' in db):
                 data = db["expenses"]
            else:
                data = ['There are no expenses rn!']     
        for i in data:
            print(i)    

    elif choice== "3":
        new_category = input("add new category: ")
        categories[max(categories)+1] = new_category
    

    elif choice== "4":
        total=0
        with shelve.open('expenses_data') as db:
            if ('expenses' in db):
                expenses = db['expenses']
                for expense in expenses:
                    total+=expense[1]
                print(total)    
            else:
                print("There are no expenses rn!")

            

    elif choice == "5":
        break        
    else:
        print("Invalid response")
