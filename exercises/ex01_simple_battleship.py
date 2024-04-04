"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__="730671723"

# exercises/ex01_simple_battleship.py


#part 1:promting for Player 1 Input

# Ask the first user to pick a secret boat location between 1 and 4

player1_input = int(input("player 1 Pick a secret boat location between 1 and 4: "))

#check if input is valid 

if player1_input <1:
        print("Error! " + " player1_input " + " is to low")   
        exit() 
elif player1_input > 4:
        print("Error "+" player1_input "+" to high")
        exit()
    


#part 2:Prompting for Player 2 Input

#Ask the second user to guess a number between 1 and 4

player2_guess = int(input("player 2 Guess a number between 1 and 4: "))

#check if input is valid

if player2_guess <1:
        print("Error! " + " player2_guess " + " is to low")
        exit()
elif player2_guess > 4:
        print("Error! "+" player2_guess "+" is to high ")
        exit()
        
    


# Part 3: Checking User Input for Match

# Assuming the secret boat location from Player 1 is stored in 'secret_location'

# Check if Player 2's guess is correct

if player2_guess == player1_input:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")


# Part 4: Printing A String of Boxes
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result = RED_BOX if player1_input == player2_guess else WHITE_BOX

emoji_string = ""
for i in range(1, 5):
    emoji_string += result if i == player2_guess else BLUE_BOX

print(emoji_string)


# End of the program

