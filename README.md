Expense Tracker
A Python-based command-line application to track personal or business expenses. This tool allows users to add, view, update, delete, and summarize expenses. Transactions are stored in a JSON file for persistence, and bulk transactions can be imported from a text file.

Features
Add Transaction: Record new expenses with details like expense type, amount, and date.

View Transactions: Display all recorded transactions in a readable format.

Update Transaction: Modify existing transactions.

Delete Transaction: Remove unwanted transactions.

Display Summary: View the total amount of all expenses.

Bulk Import: Import multiple transactions from a text file.

Installation
Clone the Repository:


git clone https://github.com/helithjay/Personal-Finance-Tracker-Using-Dictionaries-.git

cd expense-tracker

Ensure Python is Installed:

This project requires Python 3.x. You can download it from python.org.

Run the Application:
Execute the Python script to start the expense tracker:


python code.py

Usage
Main Menu:
When you run the program, you'll see a menu with the following options:


1. Read Bulk Transactions from File
2. Add Transaction
3. View Transactions
4. Update Transaction
5. Delete Transaction
6. Display Summary
7. Exit
Adding a Transaction:

Select option 2 from the menu.

Enter the expense type, amount, and date.

Viewing Transactions:

Select option 3 to see all recorded transactions.

Updating a Transaction:

Select option 4 and follow the prompts to update an existing transaction.

Deleting a Transaction:

Select option 5 and enter the expense type and index of the transaction you want to delete.

Displaying Summary:

Select option 6 to view the total amount of all expenses.

Bulk Import:

Select option 1 and provide the filename (e.g., sample.txt) to import multiple transactions at once.

Exiting the Program:

Select option 7 to exit the application.

File Structure
expense_tracker.py: The main Python script containing the logic for the expense tracker.

transactions.json: A JSON file used to store transaction data.

sample.txt: A sample text file for bulk importing transactions.

Example Files
sample.txt
Copy
Keels,9000,2024-03-05
ABC,20000,2024-12-01
transactions.json
json
Copy
{
  "Keels": [
    {
      "amount": 9200.0,
      "date": "2024-03-05"
    }
  ],
  "ABC": [],
  "Samantha Grocery": [
    {
      "amount": 4235.5,
      "date": "2024-12-05"
    }
  ]
}
Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Submit a pull request.

License
This project is open-source and available under the MIT License.

Contact
For questions or feedback, feel free to reach out:

Helith Jayasuriya: helithjayasuriya77@gmail.com

GitHub: helithjay
