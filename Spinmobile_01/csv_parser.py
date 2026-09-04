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

# Test parsing the first data row (skipping header at index 0)
if __name__ == "__main__":
    lines = read_csv_raw("sample_transactions.csv")
    third_transaction = parse_line(lines[3])
    print(third_transaction)