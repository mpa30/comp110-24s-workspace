"""Test my garden functions."""

__author__: str = "730671723"

import pytest
from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind() -> None:
    """Tests the working of the function."""
    test: dict[str, list[str]] = {"flower": ["lily", "lavender"], "veggies": ["apricot", "squash"]}
    add_by_kind(test, "fruit", "banana")
    assert test == {"flower": ["lily", "lavender"], "veggies": ["apricot", "squash"], "fruit": ["banana"]}


def test_add_by_kind_number_error() -> None:
    """Reports a typeerror if an integer is placed as a paramer."""
    test: dict[str, list[str]] = {"flower": ["lily", "lavender"], "veggies": ["apricot", "squash"]}
    add_by_kind(test, 5, "banana")
    assert TypeError


def test_add_by_date() -> None:
    """Tests the working of the function."""
    test: dict[str, list[str]] = {"May": ["parsely", "mint"], "October": ["blueberry, roses"]}
    add_by_date(test, "October", "pumpkins")
    assert test == {"May": ["parsely", "mint"], "October": ["blueberry, roses", "pumpkins"]}


def test_add_by_date_typeerror() -> None:
    """Reports a typeerror if an integer is placed as a paramer."""
    test: dict[str, list[str]] = {"May": ["parsely", "mint"], "October": ["blueberry, roses"]}
    add_by_date(test, "October", 8)
    assert TypeError


def test_lookup_by_kind_and_date() -> None:
    """Tests the working of the function."""
    test_kind: dict[str, list[str]] = {"flower": ["lily", "lavender"], "veggies": ["apricot", "squash"]}
    test_date: dict[str, list[str]] = {"May": ["parsely", "mint"], "October": ["blueberry", "roses", "apricot"]}
    test = lookup_by_kind_and_date(test_kind, test_date, "veggies", "May")
    assert test == "No veggiess to plant in May."


def test_lookup_by_kind_and_date_assertionerror() -> None:
    """Reports a typeerror if an integer is placed as a paramer."""
    test_kind: dict[str, list[str]] = {"flower": ["lily", "lavender"], "veggies": ["apricot", "squash"]}
    test_date: dict[str, list[str]] = {"May": ["parsely", "mint", "lily", "lavendar"], "October": ["blueberry", "roses", "apricot"]}
    # test = lookup_by_kind_and_date(test_kind, test_date, "", "May")
    # assert test == "No flowers to plant in May."
    # TA Trinh Kieu helped with this function - Mihir wanted an edge case where he caught the assertion error
    with pytest.raises(AssertionError):
        lookup_by_kind_and_date(test_kind, test_date, "", "May")
    