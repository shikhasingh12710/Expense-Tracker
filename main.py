from database import create_table
from expense_manager import add_expense
from analytics import monthly_report, detect_anomalies
from visualize import plot_expenses

def user_input():
    print("\n💰 Expense Tracker")
    print("-" * 30)

    txn_type = input("Enter type (income/expense): ").lower()
    category = input("Enter category (Food, Rent, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    add_expense(txn_type, category, amount, date, description)
    print("✅ Transaction added successfully!")

def main():
    create_table()

    while True:
        print("\nChoose an option:")
        print("1. Add Transaction")
        print("2. View Monthly Report")
        print("3. Detect Unusual Transactions")
        print("4. Show Expense Pie Chart")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            user_input()

        elif choice == "2":
            print("\n📊 Monthly Report:")
            print(monthly_report())

        elif choice == "3":
            print("\n🚨 Unusual Transactions:")
            print(detect_anomalies())

        elif choice == "4":
            plot_expenses()

        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
