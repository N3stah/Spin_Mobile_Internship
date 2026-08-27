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
            print("→ Add transaction (coming soon)")
        elif choice == "2":
            print("→ View transactions (coming soon)")
        elif choice == "3":
            print("→ Show balance (coming soon)")
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
