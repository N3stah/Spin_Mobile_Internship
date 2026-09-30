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

if __name__ == "__main__":
    print("July 2026 ends on Friday:", month_ends_on_friday(2026, 7))     #output: True
    print("August 2025 ends on Friday:", month_ends_on_friday(2025, 8))   #output: False