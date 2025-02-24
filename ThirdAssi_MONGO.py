from pymongo import MongoClient
import re
import datetime
from bson import ObjectId


class Expense:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

    def to_dict(self):

        return {
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

class ExpenseTracker:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["PersonalExpenseDB"]
        self.collection = self.db["expenses"]

    def add_expense(self, expense):
        self.collection.insert_one(expense.to_dict())
        print("Expense added successfully!")

    def view_all_expenses(self):
        expenses = self.collection.find()
        if expenses:
            for expense in expenses:
                print(
                    f"ID: {expense['_id']} | Description: {expense['description']} | Amount: {expense['amount']} | Date: {expense['date']}")
        else:
            print("No expenses recorded yet.")

    def view_total_expenses(self):
        """Calculate and display the total expenses."""
        total = 0
        expenses = self.collection.find()
        for expense in expenses:
            total += expense['amount']
        print(f"Total Expenses: {total}")

    def delete_expense(self, expense_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(expense_id)})
            if result.deleted_count > 0:
                print("Expense deleted successfully.")
            else:
                print("Expense not found.")
        except Exception as e:
            print(f"Error deleting expense: {e}")



    def validate_date(self, date_str):

        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_amount(self, amount):

        try:
            amount = float(amount)
            if amount > 0:
                return True
            else:
                print("Amount must be a positive number!")
                return False
        except ValueError:
            print("Invalid amount!")
            return False

    #def _validate_expense(self, expense):
     #   """Validate the expense data (amount and date)."""
      #  if expense.amount <= 0:
       #     print("Amount must be a positive number.")
        #    return False
        #if not self._is_valid_date(expense.date):
         #   print("Invalid date format. Use YYYY-MM-DD.")
          #  return False
        #return True

    #def _is_valid_date(self, date):
     #   """Check if the date is in the correct format (YYYY-MM-DD)."""
      #  return bool(re.match(r"\d{4}-\d{2}-\d{2}", date))


# Simple menu for interacting with the expense tracker
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Delete an Expense")
        print("5. Exit")

        option = input("Enter your option: ").strip()

        if option == '1':
            description = input("Enter expense description: ")
            amount = input("Enter amount: ")
            while not tracker.validate_amount(amount):
                amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            while not tracker.validate_date(date):
                date = input("Invalid date format! Please enter in YYYY-MM-DD: ")

            expense = Expense(description, float(amount), date)
            tracker.add_expense(expense)

        elif option == '2':
            tracker.view_all_expenses()

        elif option == '3':
            tracker.view_total_expenses()

        elif option == '4':
            expense_id = input("Enter the expense ID to delete: ")
            tracker.delete_expense(expense_id)

        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
