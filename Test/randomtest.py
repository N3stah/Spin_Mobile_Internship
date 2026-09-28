print("\n Simple Math Calculator By Nestah")
def calculate():
    while True:
        try:
            a = float(input("Enter a number: "))
            #Ask the user what specific math operation they want
            op = input("Enter an operator (+, -, *, /): ")
            b = float(input("Enter another number: "))
            #Conditionals to perform only the requested math
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = a / b
            elif op == "%":
                result = a % b
            elif op == "**":
                result = a ** b
            else:
                print("Error: Invalid operator selected. Try again.\n")
                continue  # Restarts the loop if a user type a symbol not listed above
            # Print the final result and break
            print(f"Result: {result}")
            break
            # Catch the specific errors that can actually occur
        except ValueError:
            print("Error: Inputs must be numeric. Please try again.\n")
        except ZeroDivisionError:
            print("Error: You cannot divide by zero. Please try again.\n")
        finally:
            print(" --- Attempt Logged ---")
# Execute the function
calculate()