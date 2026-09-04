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

# manual test
if __name__ == "__main__":
    lines = read_csv_raw("sample_transactions.csv")
    print(lines[0])   # header in .csv
    print(lines[1])   # first data row