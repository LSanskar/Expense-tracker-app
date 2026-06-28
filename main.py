import os
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
   
    def saveData(self):
        with shelve.open('Expenses_data') as db:
            db['expenses'] = self.expenses
    def loadData(self):
        with shelve.open('Expenses_data') as db:
            if "expenses" in db:
                if db["expenses"]:
                    return db['expenses']
                else:
                    return False
            else:
                return False
    def showExpense(self):
        temp_data = self.loadData()
        if temp_data:
            for i in temp_data:
                print(f"{i.name} {i.amount} {i.category}")
        else:
            print('There is no data rn')        
    def clearData(self):
        extensions = [".dat",".db",".dir",".bak"]
        file_path = []
        for i in extensions:
            file_path = f"Expenses_data"
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                pass 

categories = {1:'Groceries'
              ,2: 'Bills'
              ,3: 'Rent'
              ,4: 'Miscellaneous'}  
        
exp_manager = ExpenseManager([])

if (exp_manager.loadData()):
    exp_manager = ExpenseManager(exp_manager.loadData())

for file in os.listdir():
    print(file)



while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Add custom categories")
    print("4. Total spending")
    print("5. Delete expenses")
    print("6. Exit")

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
        exp_manager.saveData()
        print("Expense added")
            
            
    elif choice == "2":
        exp_manager.showExpense()   

    elif choice== "3":
        new_category = input("add new category: ")
        categories[max(categories)+1] = new_category
    

    elif choice== "4":
        total=0

        if exp_manager.loadData():
            for i in exp_manager.loadData():
                total+=i.amount
            print(total)
        else:
            print("no expense added yet")
    
    elif choice=="5":
        exp_manager.clearData()
        print("Data is deleted")

    elif choice == "6":
        break        
    else:
        print("Invalid response")


