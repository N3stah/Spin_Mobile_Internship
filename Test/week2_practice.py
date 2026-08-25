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
