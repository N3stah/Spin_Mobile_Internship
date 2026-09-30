"""
DSA Challenge — Fridays at Month End
Spin Mobile Internship — Pre-Project Assessment
Author: Mark Manoti Ndege
Date: September 2026
"""

import calendar
from datetime import date

def month_ends_on_friday(year, month):
    """Return True if the last day of this month is a Friday."""
    last_day_number = calendar.monthrange(year, month)[1]  #finds last day of the month
    last_date = date(year, month, last_day_number)         #having a precise date object for the last day
    return last_date.weekday() == 4

def count_for_year(year):
    """Count how many months in the given year ends with friday"""
    count = 0
    for month in range(1, 13):   # Loops through 1, 2, 3... up to 12 "months"
        if month_ends_on_friday(year, month):
            count += 1
    return count

if __name__ == "__main__":
  # print("July 2026 ends on Friday:", month_ends_on_friday(2026, 7))     #output: True
  # print("August 2025 ends on Friday:", month_ends_on_friday(2025, 8))   #output: False
    print("Total months ending on a Friday in 2026:", count_for_year(2026)) #output: 1