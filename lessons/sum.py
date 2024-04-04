"""Summing the elements of a list using different loops"""
__author__ = "730671723"


def w_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a while loop."""
    sum = 0.0  # Initialize sum
    i = 0  # Initialize counter
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a for loop."""
    sum = 0.0  # Initialize sum
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a for loop with range."""
    sum = 0.0  # Initialize sum
    for i in range(len(vals)):
        sum += vals[i]
    return sum
