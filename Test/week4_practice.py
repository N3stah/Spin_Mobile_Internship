from abc import ABC, abstractmethod

#recap on type casting, loop and conditionals, functions, and exceptions.

#Type casting
# 1. Handling string issues safely.
raw_input="678.098"
amount_float=float(raw_input)
amount_int=int(amount_float)

print(f"Float: {amount_float} | Tranguate Integer: {amount_int}")
print(float(amount_int))
print(float(amount_float))

# 2. Tasting true and falsy
empty_list = []
zero_list = [0]

print(f"Empty list evaluates to: {bool(empty_list)}")  # Output: False
print(f"List with 0 evaluates to: {bool(zero_list)}")   # Output: True

#Loop & Conditionals
# 3. For Loop with 'continue' to print even numbers
print("Even Numbers 1 to 10")
for num in range(1, 10):
    if (num % 2 != 0): #even number starts from '0' while ODD start at '1'
         continue  # Skip odd numbers
    print(num)

# 4. Match-Case Menu System inside a While Loop
print("\n--- Interactive Loop ---")
counter = 0

while True:
    counter += 1
    # Simulating choice selection
    choice = "2" if counter == 1 else "3"

    match choice:
        case "1":
            print("Selected Option One")
        case "2":
            print("Selected Option Two")
        case "3":
            print("Exiting menu loop...")
            break  # Force exit

# 5. Functions
# Global variable
currency = "kes"

# Function with a default parameter returning a tuple
def calculate_total(price, tax_rate=0.16):
    global currency  # Accessing global variable
    tax = price * tax_rate
    grand_total = price + tax
    return tax, grand_total  # Returns a packed tuple

# Calling the function and unpacking the tuple
calculated_tax, final_price = calculate_total(1000)

print(f"Tax: {currency} {calculated_tax}")
print(f"Total: {currency} {final_price}")

#Classes, init, self, class vs instance attributes
print("\n--- WEEK 2 PRACTICE ---")
class BankAccount:
    """Represents a simple bank account."""
    BANK_NAME = "Spin Mobile Bank"  # Class attribute (shared)

    def __init__(self, owner_name: str, starting_balance: float):
        # Instance attributes (unique per object)
        self.owner_name = owner_name
        self.balance = starting_balance

    def deposit(self, amount: float) -> float:
        """Adds funds to the instance balance."""
        self.balance += amount
        return self.balance

    def get_balance(self) -> float:
        """Returns current balance."""
        return self.balance


# Instantiating two unique objects
acc1 = BankAccount("Mark", 1000.99)
acc2 = BankAccount("Sarah", 2500)

acc1.deposit(500)
print(f"{acc1.owner_name} ({BankAccount.BANK_NAME}): ${acc1.get_balance()}")
print(f"{acc2.owner_name} ({BankAccount.BANK_NAME}): ${acc2.get_balance()}")

# writing a class counter that has a class attribute.
class Counter:
    total_created = 0  # Class attribute shared across all instances

    def __init__(self):
        # Increment the shared class attribute whenever a new instance is created
        Counter.total_created += 1


# Create 3 instances
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Output the shared class count
print(Counter.total_created)  # Outputs: 3

#6. Abstraction & Polymorphism
class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self) -> str:
        """Every vehicle subclass must implement its fuel type."""
        pass

class ElectricCar(Vehicle):
    def fuel_type(self) -> str:
        return "Electricity"

class PetrolCar(Vehicle):
    def fuel_type(self) -> str:
        return "Unleaded Petrol"

# Polymorphism in action: loop through distinct subclasses uniformly
vehicles = [ElectricCar(), PetrolCar()]
for m in vehicles:
    print(f"Vehicle fuel type: {m.fuel_type()}")

#7. Encapsulation & Inheritance
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self._salary = salary  # Protected attribute

    @property
    def salary(self) -> float:
        """Read-only property access."""
        return self._salary

    def get_pay(self) -> float:
        return self._salary

class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)  # Delegate name and salary to parent
        self.bonus = bonus

    def get_pay(self) -> float:
        """Override parent method to add bonus."""
        return self.salary + self.bonus

# Test implementation
emp = Employee("Mark", 50000)
mgr = Manager("Sarah", 80000, 15000)

print(f"{emp.name} Pay: ${emp.get_pay()}")
print(f"{mgr.name} Pay: ${mgr.get_pay()}")

#DRY AND KISS
# Refactor these three functions to remove the duplicated validation logic.
def validate_rate(rate):
    """Helper function to validate tax rates, keeping code DRY."""
    if rate < 0 or rate > 1:
        raise ValueError("Rate must be between 0 and 1")

def calculate_income_tax(rate, amount):
    validate_rate(rate)
    return amount * rate

def calculate_expense_tax(rate, amount):
    validate_rate(rate)
    return amount * rate

def calculate_transfer_tax(rate, amount):
    validate_rate(rate)
    return amount * rate

# SRP in Week 3 csv_parser.py

# In Week 3's csv_parser.py, I have found that the load_transactions (filepath) function violates SRP because it handles two distinct jobs:
# one, been Validating and reading the file, that  is handling FileNotFoundError and checking if it is empty.
# second, Iterating over the lines by parsing them, and catching ValueError/IndexError formatting errors.
# To be able to fully follow SRP, we could split this into a read_valid_lines(filepath) for file validation, and parse_all_rows(lines) strictly for data processing.