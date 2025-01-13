import json
expenses = []
def budgetbuddy():
    def validation(choice):
        return 1 <= choice <=6
        #if 1 <= choice <= 4:
         #   return
        #else:
         #   print("Please select a number between 1 to 4")
          #  choose()
    def add_expense():
        print("enter details about your expense below")
        expense_explanation = input("explain about your expense : ")
        expense_amount = input("how much is the expense ? ")
        expense_date = input("when was the expense ? ")
        expense_data = {
            "amount" : expense_amount,
            "date" : expense_date,
            "explanation" : expense_explanation
        }
        expenses.append(expense_data)  
        print("Expense added successfully!")
        choose()
    def edit_expense():
        if not expenses:
            print("No expenses recorded yet.")
            choose()
        view_expenses()
        try:
            choice = int(input("Which expense do you want to edit ? "))
            if 1 <= choice <= len(expenses):
                expense_explanation = input("edit the explanation of expense : ")
                expense_amount = input("edit the amount of expense : ")
                expense_date = input("edit the date of expense : ")
                expenses[choice-1]["amount"] = expense_amount
                expenses[choice-1]["date"] = expense_date
                expenses[choice-1]["explanation"] = expense_explanation
                print("expense edited successfully!")
                choose()
            else:
                print("Please enter the exact number of the expense.")
                edit_expense()
        except ValueError:
            print("Please enter a valid number.")
            edit_expense()
    def remove_expense():
        if not expenses:
            print("No expenses recorded yet.")
            choose()
        view_expenses()
        try:
            choice = int(input("which expense do you want to remove ? "))
            if 1 <= choice <= len(expenses):
                removed_expense = expenses.pop(choice-1)
                print(f"expense removed successfully! Removed : {removed_expense}")   
                choose()
            else:
                print("Please enter the exact number of the expense.")
                remove_expense()
        except ValueError:
            print("Please enter a valid number.")
            remove_expense()
    def view_expenses():
        if not expenses:
            print("No expenses recorded yet.")
            choose()
        else:
            print("Your expenses are:")
            print("")
            for index, expense in enumerate(expenses, start=1):
                print(f"""{index}.\nexplanation : {expense['explanation']}\nAmount : {expense['amount']}\ndate : {expense['date']}""")
            print("")    
            return
    def save_expenses():
        if not expenses:
            print("No expenses recorded yet.")
            choose()
        with open("expenses.json","w") as file:
            json.dump(expenses,file,indent=4)
        print("Expenses saved to 'expenses.json'!")
        choose()
    def load_expenses():
        global expenses  
        try:
            with open("expenses.json", "r") as file:
                loaded_data = json.load(file)  
                if isinstance(loaded_data, list):  
                    expenses = loaded_data
                    print("Expenses loaded successfully!")
                else:
                    print("Error: Loaded data is not in the correct format.")
        except FileNotFoundError:
            print("No saved expenses found.")
        except json.JSONDecodeError:
            print("Error: File contains invalid JSON.")
        choose()
    def greeting():
        print("\n")
        print("Hi!\nWelcome to BudgetBuddy!")
        print("This project is here to help you see your expenses, clarify them and as results help you to save.")
        print("BudgetBuddy is programmed by Faraz Moazzen.")
        print("1403/10/23")
        choose()
    def choose():
        print("")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Remove Expense")
        print("4. View Expenses")
        print("5. Save Expenses")
        print("6. load Expenses")
        print("")
        try:
            choice = int(input("choose what to do -> "))
            if not validation(choice):
                print("Please select a number between 1 to 6")
            if choice == 1:
                add_expense()
            elif choice == 2:
                edit_expense()
            elif choice == 3:
                remove_expense()
            elif choice == 4:
                view_expenses()
                choose()
            elif choice == 5:
                save_expenses()
            elif choice == 6:
                load_expenses()
        except ValueError:
            print('Please choose a valid number')
            choose()
    greeting()
budgetbuddy()