import shelve

class Expense:
    def __init__(self,name,amount,category):
        self.name = name
        self.amount = amount
        self.category = category
    
class ExpenseManager:
    def __init__(self,expenses):
        self.expenses = expenses
    def addExpense(self,expense):
        self.expenses.append(expense)
    def showExpense(self):
        for i in self.expenses:
            print(f"{i.name}, {i.amount}, {i.category}")

categories = {1:'Groceries'
              ,2: 'Bills'
              ,3: 'Rent'
              ,4: 'Miscellaneous'}  
        
exp_manager = ExpenseManager([])


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Add custom categories")
    print("4. Total spending")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        category_selector = int(input("Choose between the categories for this expense"))    
        while (not(category_selector in categories)):
            print("Enter valid response")
            category_selector = input("Choose between the categories for this expense")
        exp_selector = Expense(name,amount,categories[category_selector])

        exp_manager.addExpense(exp_selector)
        print("Expense added")
            
            
    elif choice == "2":
        exp_manager.showExpense()   

    elif choice== "3":
        new_category = input("add new category: ")
        categories[max(categories)+1] = new_category
    

    elif choice== "4":
        total=0
        if exp_manager.expenses:
            for i in exp_manager.expenses:
                total+=i.amount
            print(total)
        else:
            print("no expense added yet")
            

    elif choice == "5":
        break        
    else:
        print("Invalid response")


