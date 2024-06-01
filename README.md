# Spending Calculator

Spending Calculator is a Python application that helps you manage your expenses and track your spending. It allows you to add expenses, update your balance, view all expenses, and delete all spending data.

## Features

- Add and categorize expenses.
- Update your initial balance.
- View all recorded expenses by date and category.
- View the available balance.
- Delete all spending data.

## Requirements

- Python 3.x

## Setup

1. **Clone the repository** (if applicable) or download the script files.

2. **Create necessary directories**:
   ```sh
   mkdir spending
   
3. **Run the application**:
   ```sh
   python spending_calculator.py

## Usage

Upon running the application, you'll be prompted with the following menu:
```sql
1. Add Expense
2. Update Initial Balance
3. Delete All Spending Data
4. View All Expenses
5. View Available Balance
6. Exit
```
## Menu Options
**Add Expense**:

   -Enter the category of the expense.
   -Enter the amount spent.
   -The expense will be recorded, and your balance will be updated.
   
**Update Initial Balance**:

   -Choose whether to completely change the initial balance or add a value to the remaining balance.
   -Enter the new amount.
   
**Delete All Spending Data**:

   -Deletes all recorded spending data from the spending directory.

**View All Expenses**:

   -Displays all recorded expenses grouped by date and category.

**View Available Balance**:

   -Displays the current available balance.
**Exit**:

   -Exits the application.

## File Structure

  -balance.json: Stores the current balance.
  -spending/: Directory that contains JSON files, each representing a day's expenses.

  
## License

This project is open source and available under the MIT License.

Feel free to modify the README file as necessary to suit your needs.
