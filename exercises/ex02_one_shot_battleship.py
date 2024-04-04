# ex02_one_shot_battleship.py

"""
A simple implementation of a one-shot battleship game. The user has one chance to guess the location of a hidden ship on a 4x4 grid.
"""

__author__ = "730671723"

# Constants for the game's grid symbols
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# The game's grid size and the secret location of the ship
GRID_SIZE: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2

def get_guess(prompt: str, max_val: int) -> int:
    """
    Prompt the user for a guess within the grid bounds. Ensures the guess is valid.
    """
    while True:
        try:
            guess: int = int(input(prompt))
            if 1 <= guess <= max_val:
                return guess
            print(f"The grid is only {max_val} by {max_val}. Try again: ", end="")
        except ValueError:
            print("Invalid input. Please enter a number. Try again: ", end="")

def print_grid(row_guess: int, column_guess: int) -> None:
    """
    Print the game grid, indicating the user's guess and the result of that guess.
    """
    for row in range(1, GRID_SIZE + 1):
        for column in range(1, GRID_SIZE + 1):
            if row == row_guess and column == column_guess:
                box = RED_BOX if row == SECRET_ROW and column == SECRET_COLUMN else WHITE_BOX
            else:
                box = BLUE_BOX
            print(box, end="")
        print()  # Newline after each row

def provide_feedback(row_guess: int, column_guess: int) -> None:
    """
    Provide feedback to the player based on their guess compared to the ship's location.
    """
    if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN:
        print("Hit!")
    elif row_guess == SECRET_ROW:
        print("Close! Correct row, wrong column.")
    elif column_guess == SECRET_COLUMN:
        print("Close! Correct column, wrong row.")
    else:
        print("Miss!")

def main() -> None:
    """
    Main function to run the one-shot battleship game.
    """
    print("Welcome to One-Shot Battleship!")
    row_guess: int = get_guess("Guess a row: ", GRID_SIZE)
    column_guess: int = get_guess("Guess a column: ", GRID_SIZE)
    print_grid(row_guess, column_guess)
    provide_feedback(row_guess, column_guess)

if __name__ == "__main__":
    main()
