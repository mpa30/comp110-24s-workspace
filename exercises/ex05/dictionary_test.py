"""Unit tests for dictionary functions."""
__author__ = "730671723"

import pytest
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance

# Tests for invert
def test_invert_simple():
    assert invert({"a": "1"}) == {"1": "a"}

def test_invert_empty():
    assert invert({}) == {}

def test_invert_raises_error_for_duplicate_values():
    with pytest.raises(KeyError):
        invert({"a": "1", "b": "1"})


# Tests for favorite_color
def test_favorite_color_basic():
    assert favorite_color({"Alice": "blue"}) == "blue"

def test_favorite_color_tie():
    assert favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "blue"}) == "blue"

def test_favorite_color_no_input():
    with pytest.raises(ValueError):
        favorite_color({})


# Tests for count
def test_count_multiple_items():
    assert count(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}

def test_count_single_item():
    assert count(["a"]) == {"a": 1}

def test_count_empty():
    assert count([]) == {}

# Tests for alphabetizer
def test_alphabetizer_basic_sort():
    assert alphabetizer(["banana", "apple", "carrot"]) == {"a": ["apple"], "b": ["banana"], "c": ["carrot"]}

def test_alphabetizer_mixed_case():
    words = ["apple", "Apple", "banana", "Banana"]
    expected = {"a": ["Apple", "apple"], "b": ["Banana", "banana"]}
    assert alphabetizer(words) == expected

def test_alphabetizer_empty():
    assert alphabetizer([]) == {}

# Tests for update_attendance
def test_update_attendance_add_new():
    attendance = {}
    update_attendance(attendance, "Monday", "Alice")
    assert attendance == {"Monday": ["Alice"]}

def test_update_attendance_existing_day():
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Bob")
    assert attendance == {"Monday": ["Alice", "Bob"]}

def test_update_attendance_no_duplicates():
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Alice")
    assert attendance == {"Monday": ["Alice"]}
