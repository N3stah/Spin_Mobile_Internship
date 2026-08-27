# First practice examples
# A python command that ask users for their age and coverts it and give the future age in 5 years

age = int(input("Enter your age: "))
future_age = age + 5
print(f"In 5 years, you will be {future_age} years old.")

# 2. Ask for a price in KES, apply 16% VAT, print total
price = float(input("Enter price in Ksh: "))
total_price = price * 1.16
print(f"Total price including 16% VAT: Ksh {total_price:.2f}")  #  :   tells python to stop treating it as variable.
                                                                #  .2f  display the value to 2 decimal place.

# 3. Ask for two numbers, print their sum, difference, product and quotient.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")

# 4. Ask for a test marks scores (0-100) and print letter grade
marks_scores = float(input("Enter test score (0-100): "))
if marks_scores >= 90:
    print("Grade: A")
elif marks_scores >= 80:
    print("Grade: B")
elif marks_scores >= 70:
    print("Grade: C")
elif marks_scores >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 5. Ask for an integer and check if it is even/odd
number = int(input("Enter an integer: "))
if number % 2 == 0:                # using modulo (%)
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# 6. Check if a number is positive, negative, or zero
val = float(input("Enter any number: "))
if val > 0:
    print("Number is positive")
elif val < 0:
    print("Number is negative")
else:
    print("Number is zero")

# 7. Print numbers 1 to 10 using a for loop with range()
for i in range(1, 11):
    print(i)

# 8. Calculate the sum of numbers from 1 to 100 using a loop
total_sum = 0
for num in range(1, 101):
    total_sum += num
print(f"Sum of numbers from 1 to 100: {total_sum}")

# 9. Prompt user for input continuously until they enter 'quit'
while True:
    user_input = input("Enter something (or 'quit' to exit): ").strip().lower()
    if user_input == "quit":
        print("Goodbye!")
        break
    print(f"You typed: {user_input}")

# 10. Print a receipt for a transaction using formatted f-strings
item = "Salary"
amount = 47500.0
trans_type = "income"

print("=" * 35)
print(f"{'TRANSACTION RECEIPT':^35}")
print("=" * 35)
print(f"{'Item':<12}: {item:<20}")
print(f"{'Amount':<12}: KES {amount:>14,.2f}")
print(f"{'Type':<12}: {trans_type:<20}")
print("=" * 35)

print("\n")

# 11. Function to format full name as "LASTNAME, Firstname"
def format_name(full_name: str) -> str:
    parts = full_name.strip().split()
    first_name = parts[0].title()
    last_name = parts[-1].upper()
    return f"{last_name}, {first_name}"


# Example execution
print(format_name("Mark Manoti"))

# 12.  Number guessing game
secret_number = 69
attempts = 0

while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess < secret_number:
        print("Higher")
    elif guess > secret_number:
        print("Lower")
    else:
        print(f"Correct! It took you {attempts} attempt.")
        break


# 13. Calculate VAT with a default rates
def calculate_vat(amount: float, rate: float = 0.16) -> tuple[float, float]:
    vat_amount = amount * rate
    total = amount + vat_amount
    return round(vat_amount, 2), round(total, 2)

print(calculate_vat(100))  #uses the default 16% #output= (16.0, 116.0)
print(calculate_vat(200, 0.18)) #uses assigned 18% #output= (36.0, 236.0)

# 14. Format transaction into display string
def format_transaction(t_type: str, amount: float, description: str) -> str:
    sign = "+" if t_type.lower() == "income" else "-"
    return f"{sign} KES {amount:,.2f} | {description}"

print(format_transaction("income", 100, "june"))   #output: + KES 100.00 | june

# 15. Filter list of transaction dicts by type
def filter_by_type(transactions: list[dict], t_type: str) -> list[dict]:
    return [t for t in transactions if t.get("type") == t_type]

data = [
        {"type": "income", "amount": 5000.0, "description": "Salary payment"},
        {"type": "expense", "amount": 200.0, "description": "Bus fare"},
        {"type": "expense", "amount": 1500.0, "description": "Groceries"},
]
print("Filtered Income:" ,filter_by_type(data, "income"))
print("Filtered Expenses:", filter_by_type(data, "expense"))

class NegativeValueError(Exception):
    """Raised when a withdrawal amount exceeds the current account balance."""
    pass
class OutOfRangeError(Exception):
    """Raised when an integer input falls outside the required range."""
    pass
# 16. safe_divide function
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both inputs must be numeric.")
    finally:
        print("Division attempted.")
# 17. withdraw function using custom exception
def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise NegativeValueError(
            f"Withdrawal amount KES {amount:,.2f} exceeds balance KES {balance:,.2f}."
        )
    return balance - amount
# 18. get_valid_integer function with input loop and range checking
def get_valid_integer(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            user_input = input(prompt)
            val = int(user_input)
            if val < min_val or val > max_val:
                raise OutOfRangeError(
                    f"Number {val} is outside valid range [{min_val}, {max_val}]."
                )
            return val
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")
        except OutOfRangeError as err:
            print(err)

# Verification Tests
if __name__ == "__main__":
    print("--- 16. Testing safe_divide ---")
    safe_divide(10, 2)       #only one accepted  output: Division Attempted
    safe_divide(10, 0)     # Output: Division attempted. Error: Cannot divide by zero.
    safe_divide(10, "two")  #ouput:Division attempted.  Error: Both inputs must be numeric.

    print("\n--- 17. Testing withdraw ---")
    try:
        balance = withdraw(5000.0, 6000.0)
    except NegativeValueError as e:
        print(f"Caught expected exception: {e}")  #output: Caught expected exception: Withdrawal amount KES 6,000.00 exceeds balance KES 5,000.00.

    print("\n--- 18. Testing get_valid_integer ---")
    valid_num = get_valid_integer("Enter 1-10: ", 1, 10)
    print(f"Accepted value: {valid_num}")