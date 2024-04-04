"functional Battleship"


__author__ = "730671723"


def input_guess(size: int, spec: str) -> int:
    """Prompt for and return a row or column guess within the grid size."""
    assert spec == "row" or spec == "column", "spec must be 'row' or 'column'"
    while True:
        guess = int(input(f"Guess a {spec}: "))
        if 1 <= guess <= size:
            return guess
        print(f"The grid is only {size} by {size}. Try again.")


def print_grid(size: int, row_guess: int, column_guess: int, is_correct: bool) -> None:
    """Prints a grid of boxes, marking the guess location with the appropriate symbol."""
    HIT = "🟥"
    MISS = "⬜"
    WATER = "🟦"
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            if row == row_guess and col == column_guess:
                print(HIT if is_correct else MISS, end="")
            else:
                print(WATER, end="")
        print()  # Ensures newline after printing each row


def correct_guess(secret_row: int, secret_col: int, row_guess: int, column_guess: int) -> bool:
    """Determines if the user's guess matches the secret location."""
    return secret_row == row_guess and secret_col == column_guess


import random

def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Main game loop for Battleship, orchestrating the gameplay."""
    for turn in range(1, 6):
        print(f"=== Turn {turn}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        is_correct = correct_guess(secret_row, secret_col, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, is_correct)
        if is_correct:
            print(f"Hit!\nYou won in {turn}/5 turns!")
            return
        else:
            print("Miss!")
    print("X/5 - Better luck next time!")

if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))