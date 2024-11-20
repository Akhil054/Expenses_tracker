from expense import Expense
import calendar
import datetime

def main():
    print("Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 10000

    # Get user input for expense
    expense = get_user_expense()

    # Write their expenses to a file
    save_expense_to_(expense, expense_file_path)

    # Read and Summarize the expenses
    summarize_expense(expense_file_path, budget)


def get_user_expense():
    print("Getting the Expense")
    expense_name = input("Enter the Expense Name: ")
    expense_amount = float(input("Enter the Expense Amount: "))

    expense_categories = [
        "Food", 
        "Home", 
        "Work", 
        "Fun", 
        "Misc"
    ]

    while True:  
        print("Select the Category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"  
        selected_index = int(input(f"Enter the category No {value_range}: ")) - 1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]  
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount   
            )  
            return new_expense
        else:
            print("Invalid Category. Please try again")


def save_expense_to_(expense, expense_file_path):  
    print(f"Saving the User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expense(expense_file_path, budget):
    print("Summarizing the User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:  
        lines = f.readlines()  
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")  
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category
                )                                       
            expenses.append(line_expense)  

    amount_by_category  = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses by Category : - ",amount_by_category)

    total_spend = sum([x.amount for x in expenses])    
    print(f"Total expenses:  ${total_spend:-.2f} this month !")

    budget_left = budget - total_spend
    print(f"Budget left:   ${budget_left:-.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print("Remaining days in current month : - ",remaining_days)

    daily_budget = budget_left / remaining_days
    print(f"Budget Per Day : ${daily_budget:.2f}")


if __name__ == "__main__":
    main()

