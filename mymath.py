"""
mymath module
=============

This module provides basic arithmetic and mathematical utility functions.

Functions
---------
- add(a, b)
- multiply(a, b)
- subtract(a, b)
- divide(a, b)
- power(a, b)
- factorial(n)
- is_even(n)
- average(numbers)
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Sum of the inputs.

    Examples
    --------
    >>> add(2, 3)
    5
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first.

    Parameters
    ----------
    a : float
        Minuend.
    b : float
        Subtrahend.

    Returns
    -------
    float
        Difference of the inputs.

    Examples
    --------
    >>> subtract(5, 2)
    3
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Product of the inputs.

    Examples
    --------
    >>> multiply(4, 2)
    8
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second.

    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator.

    Returns
    -------
    float
        Result of division.

    Raises
    ------
    ValueError
        If b is zero.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """
    Raise a to the power of b.

    Parameters
    ----------
    a : float
        Base.
    b : float
        Exponent.

    Returns
    -------
    float
        a raised to the power of b.

    Examples
    --------
    >>> power(2, 3)
    8
    """
    return a ** b

def factorial(n):
    """
    Compute the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        Non-negative integer.

    Returns
    -------
    int
        Factorial of n.

    Raises
    ------
    ValueError
        If n is negative.

    Examples
    --------
    >>> factorial(5)
    120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(n):
    """
    Check if a number is even.

    Parameters
    ----------
    n : int
        Integer to check.

    Returns
    -------
    bool
        True if n is even, False otherwise.

    Examples
    --------
    >>> is_even(4)
    True
    """
    return n % 2 == 0

def average(numbers):
    """
    Compute the average of a list of numbers.

    Parameters
    ----------
    numbers : list of float
        List of numbers.

    Returns
    -------
    float
        Average value.

    Raises
    ------
    ValueError
        If the list is empty.

    Examples
    --------
    >>> average([1, 2, 3])
    2.0
    """
    if not numbers:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(numbers) / len(numbers)

