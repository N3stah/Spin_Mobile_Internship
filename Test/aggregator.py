#Python script that loops through raw_data, extracts the transaction type and the amount from each string, and calculates the total running sum for each category.

raw_data = ['income: 500', 'expense: 200', 'income: 1000', 'expense: 50']
# Step 1: Use empty dictionary to store our totals
totals = {}
# Step 2: Loop through each transaction string
for transaction in raw_data:
    # Step 3: Split the string to get [category, amount]
    parts = transaction.split(': ')
    category = parts[0]  # 'income' or 'expense'
    amount = float(parts[1])  # Convert string to float
    # Step 4: Check if category already exists in dictionary
    if category in totals:
        # If it exists, add to the running total
        totals[category] += amount
    else:
        # If it doesn't exist, create it with this amount
        totals[category] = amount
# final result
print(totals)