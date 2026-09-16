"""
OOP Reporting Pipeline — SOLID Refactor of Week 3 CSV/JSON Parser
Spin Mobile Internship — Week 4 Assessment
Author: Mark Manoti Ndege
Date: September 2026

Description:
    An extensible, object-oriented reporting pipeline that reads transaction
    data from a source, calculates metrics, and writes a formatted report.
    Refactored from the Week 3 procedural csv_parser.py following SOLID
    design principles.
"""
from abc import ABC, abstractmethod
import json

class InvalidAmountError(Exception):
    """Raised when a transaction amount is zero, negative, or otherwise invalid."""
    pass

class Transaction:
    """Represents a single financial transaction with built-in validation."""
    VALID_TYPES = ("income", "expense")
    def __init__(self, t_type, amount, description):
        """ Args: t_type (str): 'income' or 'expense'.amount (float): Transaction amount, must be positive.
         description (str): Non-empty description.
        Raises:ValueError: If t_type is invalid.InvalidAmountError: If amount is zero or negative.
        """
        t_type = t_type.strip().lower()
        if t_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid transaction type: {t_type}")

        amount = float(amount)
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

        self._type = t_type
        self._amount = amount
        self._description = description.strip()

    @property
    def type(self):
        """Read only access to the transaction type."""
        return self._type

    @property
    def amount(self):
        """Read only access to the transaction amount."""
        return self._amount

    @property
    def description(self):
        """Read-only access to the transaction description."""
        return self._description

    def __repr__(self):
        return f"Transaction({self._type}, {self._amount}, '{self._description}')"

#test
if __name__ == "__main__":
    t = Transaction("income", 5000, "Salary")
    print(t)                    #Output:(income, 5000.0, 'Salary')
    print(t.amount)             #Output: 5000.0
