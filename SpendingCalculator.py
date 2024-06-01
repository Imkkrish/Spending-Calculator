import os
import json
from datetime import date

class SpendingCalculator:
    def __init__(self):


        self.balance = self.load_balance()
        self.spending_data = self.load_spending_data()

    def load_balance(self):
        if os.path.exists("balance.json"):
            with open("balance.json", "r") as file:
                data = json.load(file)
                return data['balance']
        else:
            return float(input("Enter initial balance: Rs "))

    def load_spending_data(self):
        spending_data = {}
        for filename in os.listdir("spending"):
            with open(os.path.join("spending", filename), "r") as file:
                data = json.load(file)
                date = filename[:-5]  # Remove .json extension
                spending_data[date] = data
        return spending_data

    def save_balance(self):
        with open("balance.json", "w") as file:
            json.dump({"balance": self.balance}, file)

    def add_expense(self, category, amount):
        self.balance -= amount
        self.save_balance()
        today = date.today().strftime("%Y-%m-%d")
        if today not in self.spending_data:
            self.spending_data[today] = {}
        if category in self.spending_data[today]:
            self.spending_data[today][category] += amount
        else:
            self.spending_data[today][category] = amount
        self.save_spending_data()
        print(f"Expense of Rs {amount} added for {category}.\nRemaining balance: Rs {self.balance}")

    def update_balance(self, choice, amount):
        if choice == 1:  # Completely change the value
            self.balance = amount
        elif choice == 2:  # Add value upon remaining
            self.balance += amount
        
        self.save_balance()
        print(f"Initial balance updated to Rs {self.balance}")

    def delete_spending_data(self):
        self.spending_data = {}
        for filename in os.listdir("spending"):
            os.remove(os.path.join("spending", filename))
        print("All spending data deleted.")

    def view_all_expenses(self):
        for date, data in self.spending_data.items():
            print(f"\nExpenses on {date}:")
            for category, amount in data.items():
                print(f"{category}: Rs {amount}")
            print(f"Availabe Balance: RS{self.balance}")
    def save_spending_data(self):
        for date, data in self.spending_data.items():
            filename = os.path.join("spending", f"{date}.json")
            with open(filename, "w") as file:
                json.dump(data, file)
    def view_balance(self):
        print(f"Available balance: Rs {self.balance}")


def record_spending(calculator):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: Rs "))
    calculator.add_expense(category, amount)

def main():
    calculator = SpendingCalculator()

    while True:
        print("\n1. Add Expense")
        print("2. Update Initial Balance")
        print("3. Delete All Spending Data")
        print("4. View All Expenses")
        print("5. Available  balance ")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            record_spending(calculator)
        elif choice == '2':
            print("\n1. Completely change the initial balance")
            print("2. Add value upon remaining balance")
            update_choice = int(input("Enter your choice: "))
            new_amount = float(input("Enter new amount: Rs "))
            calculator.update_balance(update_choice, new_amount)
        elif choice == '3':
            calculator.delete_spending_data()
        elif choice == '4':
            calculator.view_all_expenses()
        elif choice == '5':
            calculator.view_balance()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter again.")

if __name__ == "__main__":
    main()
