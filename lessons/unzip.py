"""Splitting a dictionary into two lists."""

__author__ = "730671723"

from typing import Dict, List

def get_keys(input_dict: Dict[str, int]) -> List[str]:
    """Extract keys from a dictionary.

    Parameters:
        input_dict: A dictionary with string keys and integer values.

    Returns:
        A list of keys from the input dictionary. Returns an empty list if the dictionary is empty.
    """
    return list(input_dict.keys())

def get_values(input_dict: Dict[str, int]) -> List[int]:
    """Extract values from a dictionary.

    Parameters:
        input_dict: A dictionary with string keys and integer values.

    Returns:
        A list of values from the input dictionary. Returns an empty list if the dictionary is empty.
    """
    return list(input_dict.values())
