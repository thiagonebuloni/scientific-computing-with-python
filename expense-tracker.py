def add_expense(expenses: list, amount: float, category: str):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses: list):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses: list) -> float:
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses: list, category: str) -> list:
    return filter(lambda expense: expense['category'] == category, expenses) # type: ignore
    

def main():
    expenses: list = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice: str = input('Enter your choice: ')

        if choice == '1':
            amount: float = float(input('Enter amount: '))
            category: str = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category: str = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category: list = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break

main()