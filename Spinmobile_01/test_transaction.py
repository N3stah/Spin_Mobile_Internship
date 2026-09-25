from oop_pipeline import Transaction

def test_transaction_creation():
    """Test that a transaction is created with the correct encapsulated attributes."""
    # 1. Provide sample input with messy capitalization and extra spaces
    t = Transaction(" Income ", 5000, "   Salary   ")

    # 2. Use 'assert' to boldly claim what the result SHOULD be
    assert t.type == "income"  # Should be lowercased and stripped
    assert t.amount == 5000.0  # Should be a float
    assert t.description == "Salary"  # Should be stripped of whitespace