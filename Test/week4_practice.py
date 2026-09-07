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
