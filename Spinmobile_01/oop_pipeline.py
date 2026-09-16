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

class DataSource(ABC):
    """
    Abstract base class for any transaction data source.

    Any concrete data source (CSV, JSON, database, API) must implement
    load() and return a list of Transaction objects. This lets the rest
    of the pipeline work with ANY data source without knowing which one.
    """

    @abstractmethod
    def load(self):
        """  Load and return transactions from this source.
        Returns:
            list[Transaction]: Parsed and validated transactions.
        """
        pass

class CSVDataSource(DataSource):
    """Loads transactions from a CSV file."""

    def __init__(self, filepath):
        self._filepath = filepath

    def load(self):
        """  Read the CSV file and return a list of Transaction objects.
        Skips malformed rows with a warning instead of crashing.
        Returns:
            list[Transaction]: Successfully parsed transactions.
        """
        try:
            with open(self._filepath, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"File not found: {self._filepath}")
            return []

        if not lines:
            print("File is empty.")
            return []

        transactions = []
        skipped = 0

        # Time complexity: O(n) — one pass through n data rows
        for i, line in enumerate(lines[1:], start=2):
            if not line.strip():
                continue
            try:
                fields = line.strip().split(",")
                # Here we use our new class instead of a dictionary!
                transaction = Transaction(fields[0], fields[1], fields[2])
                transactions.append(transaction)
            except (ValueError, IndexError, InvalidAmountError) as e:
                print(f"Skipping row {i}: {e}")
                skipped += 1

        print(f"Parsed {len(transactions)} transactions, skipped {skipped} malformed row(s).")
        return transactions

class MetricsCalculator:
    """Calculates summary metrics from a list of Transaction objects."""
    def calculate(self, transactions):
        """  Args:
            transactions (list[Transaction]): Transactions to analyze.
        Returns:
            dict: Summary metrics.
        """
        if not transactions:
            return self._empty_metrics()

        total_income = 0
        total_expenses = 0
        unique_types = set()

        # Time complexity: O(n) — single pass
        for t in transactions:
            unique_types.add(t.type)
            if t.type == "income":
                total_income += t.amount
            elif t.type == "expense":
                total_expenses += t.amount

        count = len(transactions)
        average = (total_income + total_expenses) / count if count else 0

        return {
            "total_income": round(total_income, 2),
            "total_expenses": round(total_expenses, 2),
            "net_balance": round(total_income - total_expenses, 2),
            "transaction_count": count,
            "average_amount": round(average, 2),
            "unique_types": sorted(unique_types)
        }

    def _empty_metrics(self):
        """Return a zeroed-out metrics dict for an empty transaction list."""
        return {
            "total_income": 0, "total_expenses": 0, "net_balance": 0,
            "transaction_count": 0, "average_amount": 0, "unique_types": []
        }

class ReportWriter(ABC):
    """Abstract base class for writing a metrics report to any output format."""
    @abstractmethod
    def write(self, metrics, output_path):
        """ Write the metrics dict to the given output path.
        Args:
            metrics (dict): Summary metrics to write.
            output_path (str): Destination file path.
        """
        pass

class JSONReportWriter(ReportWriter):
    """Writes a metrics report as a formatted JSON file."""
    def write(self, metrics, output_path):
        """Write metrics as indented JSON."""
        with open(output_path, "w") as f:
            json.dump(metrics, f, indent=2)
        print(f"Summary written to {output_path}")

class PrettyJSONReportWriter(JSONReportWriter):
    """ Extends JSONReportWriter to also print a human-readable console summary.
    """
    def write(self, metrics, output_path):
        """Print a formatted console summary, then write JSON (overridden)."""
        print("\n--- Report Summary ---")
        for key, value in metrics.items():
            print(f"  {key}: {value}")

        super().write(metrics, output_path)   #it calls the parent's write()