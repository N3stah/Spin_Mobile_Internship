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

def count_last_friday_months(year1, year2=None):
    """ Count how many months end on a Friday between year1 and year2 (inclusive).
    If year2 is not provided, count only count the year provided with"""
    if year2 is None:
        year2 = year1  # single year case

    count = 0
    for year in range(year1, year2 + 1):
        count += count_for_year(year)

    return count

if __name__ == "__main__":
    # print("July 2026 ends on Friday:", month_ends_on_friday(2026, 7))     #output: True
    # print("August 2025 ends on Friday:", month_ends_on_friday(2025, 8))   #output: False
   #print("Total months ending on a Friday in 2026:", count_for_year(2026))  # output: 1
    print("Fridays at month end (1901-2000):", count_last_friday_months(1901, 2000)) #output: 171