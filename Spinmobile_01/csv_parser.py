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
            print(f"⚠ Skipping row {i}: {e}")
            skipped += 1

    print(f"✓ Parsed {len(transactions)} transactions, skipped {skipped} malformed row.")
    return transactions

if __name__ == "__main__":
    transactions = load_transactions("sample_transactions.csv")
    for t in transactions:
        print(t)