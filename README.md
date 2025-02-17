# Personal Finance Tracker

## Overview
This Python-based Personal Finance Tracker helps users manage their expenses by allowing them to record, update, delete, and analyze financial transactions. The program supports both individual transaction entries and bulk transaction uploads from a file.

## Features
- Read bulk transactions from a text file.
- Add new transactions with category, amount, and date.
- View all transactions by category.
- Update existing transactions.
- Delete transactions.
- Display a summary of total expenses.
- Data is stored in a JSON file for persistence.

## Installation
1. Ensure you have Python installed on your system.
2. Clone this repository or download the script.
3. Install dependencies (if any).
4. Run the script using the command:
   ```sh
   python filename.py
   ```

## Usage
### Running the Program
Execute the script using Python. The main menu provides several options for managing transactions.

### Adding Transactions
- Users can manually input transactions by specifying:
  - Type of expense
  - Amount
  - Date (YYYY-MM-DD)

### Reading Bulk Transactions
- Provide a filename (e.g., `sample.txt`) containing comma-separated values:
  ```
  Expense_Type,Amount,Date
  Keels,9000,2024-03-05
  ABC,20000,2024-12-01
  ```

### Viewing Transactions
- Displays transactions grouped by expense category.

### Updating Transactions
- Users can modify the amount and date of an existing transaction.

### Deleting Transactions
- Allows removal of a transaction based on category and index.

### Displaying Summary
- Shows total expenses calculated from all transactions.

## Data Storage Format
Transactions are stored in a JSON file (`transactions.json`) with the following structure:
```json
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
```

## Notes
- Ensure the file `transactions.json` exists before running the program.
- Transactions must be properly formatted in the bulk upload file.

## License
This project is open-source and free to use under the MIT License.

