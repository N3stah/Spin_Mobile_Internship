import json
import time

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

#Tuples, Sets & Dictionaries

# 4. Dictionary CRUD Operations
transaction = {"type": "expense", "amount": 1500}
print("\nInitial Dict:", transaction)

"""Create: add new key"""
transaction["description"] = "Office Supplies"
print("After Add   :", transaction)

"""modify existing key"""
transaction["amount"] = 1800
print("After Update:", transaction)

"""Delete: remove key"""
del transaction["description"]
print("After Delete:", transaction)

# 5. Set Operations
file1_types = ["income", "expense", "transfer", "expense"]
file2_types = ["expense", "investment", "income"]

set1 = set(file1_types)
set2 = set(file2_types)

common_types = set1 & set2
unique_to_file1 = set1 - set2

print("\nCommon types      :", common_types)
print("Unique to file 1  :", unique_to_file1)

# 6. Safe Field Retrieval Function
def get_field(record, field, default=None):
    return record.get(field, default)

sample_record = {"name": "Spin Mobile", "role": "Intern"}
print("\nFetched 'role'   :", get_field(sample_record, "role", "N/A"))
print("Fetched 'salary' :", get_field(sample_record, "salary", "N/A"))

# File IO: Reading & Writing Flat Files
# 7. Writing and Appending to Flat Text Files
file_name = "notes.txt"

# 'w' mode opens a file for writing (creates a new file or overwrites existing content)
with open(file_name, "w") as f:# Using 'with open()' guarantees the file closes automatically when the block finishes
                               # 'w' mode opens a file for writing (creates a new file or overwrites existing content)
    f.write("Line 1: Setting up week 3 practice notes.\n")
    f.write("Line 2: Practicing context managers.\n")

# 'a' mode appends new content to the end without erasing existing text
with open(file_name, "a") as f:
    f.write("Line 3: Appended entry using 'a' mode.\n")
    f.write("Line 4: Final note appended successfully.\n")

# 'r' mode opens the file for reading line-by-line (memory-efficient)
print("\n--- Full Contents of notes.txt ---")
with open(file_name, "r") as f:
    for line in f:
        # .strip() removes whitespace and trailing newline characters (\n)
        print(line.strip())

# 8. Manual CSV Creation and Line-by-Line Parsing
csv_file = "users.csv"

with open(csv_file, "w") as f:  # Manually build a CSV file with a header row and 3 records
    f.write("name,age\n")
    f.write("Mark,24\n")
    f.write("Judy,26\n")
    f.write("Abbie,22\n")

print("\n--- Parsed CSV Output ---")
with open(csv_file, "r") as f:
    lines = f.readlines()      # f.readlines() reads all lines into a Python list of strings
      # Extract and inspect header fields
header = lines[0].strip().split(",")  # ['name', 'age']

for line in lines[1:]:   # Process remaining lines by slicing from index 1 onward to skip the header
    # Strip whitespace and split string by comma separator into a list
    fields = line.strip().split(",")
    name, age = fields  # Unpack list elements directly into variables
    print(f"Name: {name}, Age: {age}")

#JSON: Structured Tree Data
# 9. Transaction Summary Serialization (dict -> JSON file -> dict)
summary_data = {
    "total_income": 12500.50,
    "total_expenses": 3400.20,
    "transaction_count": 18,
    "is_verified": True,
    "notes": None  # Serializes to 'null' in JSON
}
summary_file = "summary.json"

# 'json.dump()' writes a Python object directly to a file handle
# 'indent=2' formats the output with 2-space indentation for human readability
with open(summary_file, "w") as f:
    json.dump(summary_data, f, indent=2)

print("--- Data Written to summary.json ---")

# 'json.load()' reads a JSON file directly into a Python dictionary
with open(summary_file, "r") as f:
    reloaded_summary = json.load(f)

print("Reloaded Summary Dict:", reloaded_summary)
print("Verified Status     :", reloaded_summary["is_verified"])


# 2. Nested JSON Tree Structures
student_record = {
    "student": {
        "name": "Mark",
        "scores": [85, 90, 78]
    }
}

student_file = "student.json"

# Write nested dict to file
with open(student_file, "w") as f:
    json.dump(student_record, f, indent=2)

# Load and query nested structure
with open(student_file, "r") as f:
    reloaded_student = json.load(f)

# Accessing nested list elements via standard dict keying and list indexing
second_score = reloaded_student["student"]["scores"][1]
print("\nStudent Name :", reloaded_student["student"]["name"])
print("Second Score :", second_score)  # Output: 90

#Big-O Notation & Complexity Awareness

# 10 Benchmarking Search Performance: List O(n) vs Set O(1)
# Create a large dataset
big_list = list(range(100000))
big_set = set(big_list)
target = 99999  # Target placed at the very end to force worst-case search

# Benchmark O(n) search in List (scans items sequentially)
start_time = time.perf_counter()
found_in_list = target in big_list
list_duration = time.perf_counter() - start_time

# Benchmark O(1) search in Set (uses hash table lookup)
start_time = time.perf_counter()
found_in_set = target in big_set
set_duration = time.perf_counter() - start_time

print(f"\nlist search O(n) took: {list_duration:.6f} seconds")
print(f"Set search  O(1) took: {set_duration:.6f} seconds")

# 11. Time vs Space Trade-off Demonstration
# Dataset with 2,000 items and a single duplicate value (100)
sample_data = list(range(2000)) + [100]

# Slow approach: O(n^2) time complexity, O(1) extra space (nested loops)
def has_duplicate_slow(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

# Fast approach: O(n) time complexity, O(n) extra space (uses a 'seen' set)
def has_duplicate_fast(items):
    seen = set()  # Allocating extra memory to gain speed
    for item in items:
        if item in seen:  # O(1) average lookup
            return True
        seen.add(item)
    return False

start_slow = time.perf_counter()
has_duplicate_slow(sample_data)
slow_time = time.perf_counter() - start_slow

start_fast = time.perf_counter()
has_duplicate_fast(sample_data)
fast_time = time.perf_counter() - start_fast

print(f"\nSlow duplicate check O(n^2): {slow_time:.6f} seconds")
print(f"Fast duplicate check O(n)  : {fast_time:.6f} seconds")