#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ExpenseTracker:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = []
        self.category_totals = {}  # Track total expenses per category

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})
        
        # Update category totals
        if category in self.category_totals:
            self.category_totals[category] += amount
        else:
            self.category_totals[category] = amount
        
        self.check_budget()

    def check_budget(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        if total_expenses > self.budget:
            overspend = total_expenses - self.budget
            print(f"⚠️ Budget Alert! Exceeded by ${overspend:.2f}")
        else:
            remaining = self.budget - total_expenses
            print(f"✅ Budget OK. Remaining: ${remaining:.2f}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\n--- All Expenses ---")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. Category: {expense['category']}, Amount: ${expense['amount']:.2f}")

    def view_summary(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        print("\n--- Budget Summary ---")
        print(f"Total Budget: ${self.budget:.2f}")
        print(f"Total Spent: ${total_expenses:.2f}")
        print(f"Remaining: ${self.budget - total_expenses:.2f}")
        
        # Display category-wise totals
        print("\n--- Category Breakdown ---")
        if not self.category_totals:
            print("No category expenses yet.")
        else:
            for category, total in self.category_totals.items():
                print(f"{category}: ${total:.2f}")
        print("--------------------------")


def main():
    print("🤑 Expense Tracker with Budget Alerts 🚨")
    budget = float(input("Enter your monthly budget: $"))
    tracker = ExpenseTracker(budget)

    while True:
        print("\nOptions:")
        print("1. ➕ Add Expense")
        print("2. 📜 View Expenses")
        print("3. 📊 View Summary")
        print("4. ❌ Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            amount = float(input("Enter amount: $"))
            category = input("Category (e.g., Food, Rent): ").strip().title()
            tracker.add_expense(amount, category)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.view_summary()
        elif choice == "4":
            print("Goodbye! 💸")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


# In[ ]:




