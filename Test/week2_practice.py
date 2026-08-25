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

