"""Module for implementing various dictionary-related functions."""
__author__ = '730671723'

from typing import Dict, List

def invert(input_dict: Dict[str, str]) -> Dict[str, str]:
    """Inverts the keys and values of the input dictionary, throwing an error on duplicate values."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate value found when attempting to invert dictionary: {value}")
        inverted_dict[value] = key
    return inverted_dict

def favorite_color(names_and_colors: Dict[str, str]) -> str:
    """Determines the most frequently occurring color. In case of a tie, returns the first encountered."""
    color_counts = {}
    for color in names_and_colors.values():
        color_counts[color] = color_counts.get(color, 0) + 1
    max_count = max(color_counts.values())
    for color, count in names_and_colors.items():
        if color_counts[count] == max_count:
            return count

def count(values: List[str]) -> Dict[str, int]:
    """Counts the frequency of each unique value in a list."""
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts



def update_attendance(attendance: Dict[str, List[str]], day: str, student: str) -> None:
    """Updates or adds a student's attendance for a specific day, avoiding duplicate entries."""
    attendance.setdefault(day, [])
    if student not in attendance[day]:
        attendance[day].append(student)



def alphabetizer(words: List[str]) -> Dict[str, List[str]]:
    """Organizes words by their starting letter into a dictionary, sorting the lists of words alphabetically."""
    categorized_words: Dict[str, List[str]] = {}
    for word in words:
        key = word[0].lower()  # Ensures case insensitivity.
        categorized_words.setdefault(key, []).append(word)
    for key in categorized_words:
        categorized_words[key] = sorted(categorized_words[key], key=str.casefold)  # Sorts case-insensitively.
    return categorized_words

