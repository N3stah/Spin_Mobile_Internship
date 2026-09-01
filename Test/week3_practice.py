#Deep Indexing & Slicing
# 1. String Slicing
sentence = "Spin Mobile Internship 2026"
print("First 5 chars:", sentence[:5])
print("Last 5 chars :", sentence[-5:])
print("Reversed     :", sentence[::-1])

# 2. List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first_half = numbers[:5]
second_half = numbers[5:]
every_3rd = numbers[::3]

print("\nFirst half :", first_half)
print("Second half:", second_half)
print("Every 3rd  :", every_3rd)

# 3. List Comprehension Practice
transactions = [
    {"desc": "Salary", "amount": 5000},
    {"desc": "Coffee", "amount": 150},
    {"desc": "Laptop", "amount": 1200},
    {"desc": "Cab", "amount": 450}
]

high_value_desc = [t["desc"] for t in transactions if t["amount"] > 1000]
print("\nHigh-value descriptions (>1000):", high_value_desc)
low_value_disc = [t["desc"]for t in transactions if t["amount"] < 500]
print("Low value descriptions (<500):", low_value_disc)