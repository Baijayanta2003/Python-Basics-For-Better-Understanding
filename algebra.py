"""
algebra module
==============

Simple algebraic operations.
"""

def power(x, n):
    """Return x raised to the power of n."""
    return x ** n

def square_root(x):
    """Return the square root of x."""
    if x < 0:
        raise ValueError("x must be non-negative.")
    return x ** 0.5

