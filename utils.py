"""
utils module
============

Helper utility functions.
"""

def is_even(n):
    """Check if n is even."""
    return n % 2 == 0

def average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("Empty list.")
    return sum(numbers) / len(numbers)

