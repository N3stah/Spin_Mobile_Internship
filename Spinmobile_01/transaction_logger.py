"""
CLI Financial Transaction Logger
Spin Mobile Internship — Week 2 Assessment
Author: Mark Manoti Ndege
Date: August 2026

Description:
    A command-line tool to log, view, and track financial transactions
    with full input validation and error handling.
"""
class InvalidAmountError(Exception):
    """Raised when a transaction amount is zero, negative, or otherwise invalid."""
    pass

def show_menu():
    """Display the main application menu."""
    print("\n" + "-" * 30)
    print("   MENU")
    print("-" * 30)
    print("   1. Add Transaction")
    print("   2. View Transactions")
    print("   3. Show Balance")
    print("   4. Exit")
    print("-" * 30)

def get_valid_amount():
    """ Prompt user for a transaction amount with full validation.
    Returns:
        float: A positive transaction amount in KES.
    Raises:
        InvalidAmountError: If the amount is zero or negative."""

    while True:
        try:
            raw = input("Enter amount in(KES): ").strip()
            amount = float(raw)
            if amount <= 0:
                raise InvalidAmountError("Amount must be greater than zero .")
            return amount
        except ValueError:
            print(" Invalid input — please enter a numeric amount (e.g. 1500.00).")
        except InvalidAmountError as e:
            print(f" {e}")

def get_valid_type():
    """Prompt user for transaction type (income or expense)."""
    while True:
        t_type = input("Type (income/expense): ").strip().lower()
        if t_type in ("income", "expense"):
            return t_type
        print("Please enter 'income' or 'expense'.")

def get_valid_description():
    """Prompt user for a non-empty description."""
    while True:
        description = input("Description: ").strip()
        if description:
            return description
        print("Description cannot be empty.")


def add_transaction(transactions):
    """ Collect transaction details from user and add to the transactions list.
    Args:
        transactions (list): The running list of all transactions."""
    print("\n--- Add New Transaction ---")

    t_type = get_valid_type()
    amount = get_valid_amount()
    description = get_valid_description()

    transaction = {
        "type": t_type,
        "amount": amount,
        "description": description
    }

    transactions.append(transaction)
    print(f"Added: {t_type.upper()} of KES {amount:,.2f} — {description}")

def view_transactions(transactions):
    """Display all recorded transactions in a formatted table."""
    print("\n---Transaction History ---")

    if not transactions:
        print("No transactions recorded yet.")
        return

    print(f"\n{'#':<5} {'TYPE':<10} {'AMOUNT(KES)':>15}   {'DESCRIPTION'}")
    print("─" * 55)

    for i, t in enumerate(transactions, start=1):
        sign = "+" if t["type"] == "income" else "-"
        amount_str = f"{sign}KES {t['amount']:>10,.2f}"
        print(f"{i:<5} {t['type'].upper():<10} {amount_str}   {t['description']}")

    print("─" * 55)
    print(f"Total transactions: {len(transactions)}")

def main():
    """Main application entry point. Manages the transaction list."""
    transactions = []
    print("=" * 45)
    print("    KES Financial Transaction Logger")
    print("=" * 45)
    print("Application started.")

    while True:
        show_menu()
        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            print("→ Show balance (coming soon)")
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
