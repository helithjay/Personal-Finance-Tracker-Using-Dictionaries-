import json

# Global dictionary to store transactions
transactions = {}

# File handling functions
def load_transactions():
    global transactions
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = {}

def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=2)

def read_bulk_transactions_from_file(filename):
    global transactions
    try:
        with open(filename, 'r') as file:
            for line in file:
                line2=line.strip()
                new_line=line2.split(",")
                expense_type=new_line[0]
                amount=float(new_line[1])
                date=new_line[2]
                new_transaction = {"amount": amount, "date": date}
                if expense_type in transactions:
                    transactions[expense_type].append(new_transaction)
                else:
                    transactions[expense_type] = [new_transaction]
                save_transactions()
        print("Transaction added successfully!")

    except FileNotFoundError:
        print(filename,"Not found")

# Feature implementations
def add_transaction():
    global transactions
    try:
        expense_type = input("Enter type of expense: ")
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        new_transaction = {"amount": amount, "date": date}
        if expense_type in transactions:
            transactions[expense_type].append(new_transaction)
        else:
            transactions[expense_type] = [new_transaction]
        save_transactions()
        print("Transaction added successfully!")


    except ValueError:
        print("Enter valid details")

def view_transactions():
    global transactions
    for expense_type, expenses in transactions.items():
        print(expense_type + ":")
        for expense in expenses:
            print(f"  Amount: {expense['amount']}, Date: {expense['date']}")

def update_transaction():
    global transactions
    view_transactions()
    try:
        expense_type = input("Enter type of expense to update: ")
        if expense_type in transactions:
            index = int(input("Enter index of transaction to update: "))-1
            new_amount = float(input("Enter new amount: "))
            new_date = input("Enter new date (YYYY-MM-DD): ")
            transactions[expense_type][index]["amount"] = new_amount
            transactions[expense_type][index]["date"] = new_date
            save_transactions()
            print("Transaction updated.")
        else:
            print("Expense type not found.")
    except ValueError:
        print("Enter Valid Details")

def delete_transaction():
    global transactions
    view_transactions()
    expense_type = input("Enter type of expense to delete: ")
    if expense_type in transactions:
        index = int(input("Enter index of transaction to delete: "))-1
        del transactions[expense_type][index]
        save_transactions()
        print("Transaction deleted successfully!")
    else:
        print("Expense type not found.")
     

def display_summary():
    global transactions
    total_amount=0
    for expense_type,transactions_list in transactions.items():
        for transaction in transactions_list:
            total_amount += transaction["amount"]

    print("Total Expense is:",total_amount)
    
def main_menu():
    load_transactions()
    while True:
        print("\nMain Menu:")
        print("1. Read Bulk Transactions from File")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Display Summary")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter filename(filename.txt): ")
            read_bulk_transactions_from_file(filename)
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            update_transaction()
        elif choice == "5":
            delete_transaction()
        elif choice == "6":
            display_summary()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
