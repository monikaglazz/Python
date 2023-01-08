import random
import time

# List of possible choices in classic game
possible_choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

# List of win-lose
score_map = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

# List to storage the score
score_of_match = {'Gamer': 0, 'Computer': 0}


def instruction():
    """Prints instruction to the game."""

    print("""\nInstruction:
        -> Paper covers Rock,
        -> Rock crushes Scissors,
        -> Scissors cuts Paper """)


# The main function that handle the game
def play_the_game():
    """All steps of game."""

    print("\nLet's play!")

    instruction()

    while True:

        print("""\n---------------------------\nMENU\n---------------------------
        \nEnter:
        -> Help - to show instructions again,
        -> Rock / Paper / Scissors - to play
        -> Exit - to quit the game """)

        print()

        # Player choses the move
        gamer_choice = input("Your choice: ")

        match gamer_choice.lower():
            case 'help':
                instruction()
                continue
            case 'rock':
                player_move = 0
            case 'paper':
                player_move = 1
            case 'scissors':
                player_move = 2
            case 'exit':
                break
            case _:
                print("\nWrong input! Read carefully the menu.")
                continue

        print("\nNow computer is doing a move...")
        time.sleep(1)

        # Get random computer move
        computer_move = random.randint(0, 2)

        print("\nComputer decided for:", possible_choices[computer_move])

        # Looking for the winner
        winner = score_map[player_move][computer_move]

        if winner == player_move:
            print("\nYou've won! :)\n")
            score_of_match["Gamer"] = score_of_match["Gamer"] + 1
        elif winner == computer_move:
            print("\nComputer won! :(\n")
            score_of_match["Computer"] = score_of_match["Computer"] + 1
        else:
            print("\nIt's a tie!\n")

        print("Current score: \n\nComputer:",
              score_of_match["Computer"], "You:", score_of_match["Gamer"])


# main part of the game

print("""\n Hello in Rock, Paper, Scissors Game! """)
while True:

    print("""\nWhat do you want to do?
        1 - Play
        2 - Quit""")

    try:
        choice = int(input("""\nYour choice: """))
    except ValueError:
        print("\nWrong choice! You can choose only 1 or 2!")
        continue

    if choice == 1:
        play_the_game()
    elif choice == 2:
        print("\nBye Bye!")
        break
    else:
        print("\nWrong choice! You can only choose 1 or 2.")
