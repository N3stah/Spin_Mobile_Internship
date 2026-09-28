# Development Log

## Date: September 25, 2026
**What I did:** Wrote an automated unit test using `pytest` to verify that the `Transaction` class correctly instantiates and formats its attributes.
**What confused me:** The test failed with `AttributeError: 'Transaction' object has no attribute 't_type'`. 
**How I figured it out:** I looked closely at the `pytest` failure summary, which actually suggested `Did you mean: 'type'?`. I realized that while the internal parameter was named `t_type` in the constructor, I had encapsulated it using a `@property` decorator named `type`. I updated the assertion to `assert t.type == "income"` and the test passed.

# Development Log
## Date: September 28, 2026
**What I did:** 
Built an interactive command-line math calculator (`randomtest.py`) using `try/except/finally` blocks to handle invalid user inputs without crashing the program.
**What confused me:** 
The program was still crashing when I entered text instead of numbers, and my exception handling wasn't working. I originally tried stacking multiple `try` statements back-to-back for each math operation and tried to catch a non-existent `CalculationError`.
**ERROR:** 
`ValueError` (from converting input to float before the try block) and `SyntaxError` (from stacking `try` blocks without matching `except` blocks).
**How I figured it out:** 
I learned three critical rules about exception handling in Python:
1. **Dangerous Code Placement:** `float(input())` is "dangerous" and must be placed *inside* the `try` block to safely catch text/typing errors.
2. **No Stacking:** Every `try` block must be immediately followed by an `except` or `finally` block. 
3. **Built-in Exceptions:** You must use standard Python exceptions like `ZeroDivisionError` instead of making up names like `CalculationError`.

**What I did:** Built a data aggregator script (`Test/aggregator.py`) to parse raw text data (`'income: 500'`), extract the categories and amounts, and calculate running totals using a dictionary.
**What confused me:** I had to make sure I didn't trigger a `KeyError` by trying to add an amount to a category that didn't exist in the dictionary yet.
**How I figured it out:** I used a string `.split(': ')` method to separate the text from the number and cast the number to a `float`. To handle the dictionary safely, I initially used an `if category in totals:` block to check if the key existed before adding to it.
I then learned the "Pythonic" shortcut to do this in a single line without `if/else` statements using the `.get()` method:
`totals[category] = totals.get(category, 0) + amount`