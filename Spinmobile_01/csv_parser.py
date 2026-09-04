"""
CSV Transaction Parser & JSON Summary Generator
Spin Mobile Internship — Week 3 Assessment
Author: Mark Manoti Ndege
Date: September 2026

Description:
    Reads a raw CSV of financial transactions, computes key metrics,
    and outputs a clean JSON summary file.
"""

import json

def read_csv_raw(filepath):
    """ Read a CSV file and return a list of raw lines.
    Args:
        filepath(str): Path to the CSV file.
    Returns:
        list[str]: Raw lines from the file, including the header.
    Raises:
        FileNotFoundError: If the file does not exist."""
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines

def parse_line(line):
    fields = line.strip().split(",")
    t_type = fields[0].strip().lower()
    amount = float(fields[1].strip())
    description = fields[2].strip()

    return {
        "type": t_type,
        "amount": amount,
        "description": description
    }

def load_transactions(filepath):
    try:
        lines = read_csv_raw(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    if not lines:
        print("File is empty.")
        return []

    transactions = []
    skipped = 0

    # Time complexity: O(n) — one pass through n data rows
    for i, line in enumerate(lines[1:], start=2):  # start=2: header is row 1
        if not line.strip():
            continue
        try:
            transactions.append(parse_line(line))
        except (ValueError, IndexError) as e:
            print(f" Skipping row {i}: {e}")
            skipped += 1

    print(f" Parsed {len(transactions)} transactions, skipped {skipped} malformed row.")
    return transactions

def calculate_metrics(transactions):
    if not transactions:
        return {
            "total_income": 0,
            "total_expenses": 0,
            "net_balance": 0,
            "transaction_count": 0,
            "average_amount": 0,
            "unique_types": []
        }

    # Time complexity: O(n) each — three separate passes over n transactions
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    unique_types = {t["type"] for t in transactions}   # set comprehension

    count = len(transactions)
    total_amount = sum(t["amount"] for t in transactions)
    average = total_amount / count if count else 0

    return {
        "total_income": round(total_income, 2),
        "total_expenses": round(total_expenses, 2),
        "net_balance": round(total_income - total_expenses, 2),
        "transaction_count": count,
        "average_amount": round(average, 2),
        "unique_types": sorted(unique_types)
    }

def write_summary(metrics, output_path):
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Summary written to {output_path}")
    #Main entry point

def main():
    """Main entry point: parse CSV, calculate metrics, write JSON summary."""
    input_path = "sample_transactions.csv"
    output_path = "transaction_summary.json"

    print(f"Reading transactions from {input_path}...")
    transactions = load_transactions(input_path)

    if not transactions:
        print("No transactions to process. Exiting.")
        return

    print("Calculating metrics...")
    metrics = calculate_metrics(transactions)

    print("\n--- Summary ---")
    for key, value in metrics.items():
        print(f"  {key}: {value}")

    write_summary(metrics, output_path)

if __name__ == "__main__":
    main()