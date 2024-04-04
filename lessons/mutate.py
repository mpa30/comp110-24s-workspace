"""Mutating functions."""


__author__= "730671723"


def manual_append(numbers: list[int], value: int) -> None:
    """Appends value to the end of numbers list."""
    numbers.append(value)


def double(numbers: list[int]) -> None:
    """Doubles the value of every element in the numbers list."""
    i = 0  # Initialize counter to 0
    while i < len(numbers):
        numbers[i] *= 2  # Double the value at the current index
        i += 1  # Move to the next index


# For manual_append
a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)  # Output: [1, 2, 3, 2]


# For double
a: list[int] = [1, 2, 3]
double(a)
print(a)  # Output: [2, 4, 6]