# Bulls and Cows game is played between two players where each player chooses a 4 digit number with distinct
# non-zero digits as a secret number and players take turns to guess their opponent's secret number.
# In each turn a player guesses a number and the opponent should respond how many digits in the guessed number
# has matched with their secret number in the form of Bulls and Cows. If the matching digits are in their right
# positions, they are Bulls, if in different positions, they are Cows.
#
# For example:
#
# Secret number: 4271
# Opponent's try: 1234
# Answer: 1 bull and 2 cows
# (The bull is "2", the cows are "4" and "1".)

import random


#  Dictionary to storage all data from every attempt
cows_and_bulls = {}


#  Basic info about the games and rules
def game_rules():
    print("""\n
    Bulls and Cows game is played between two players where each player chooses 
    a 4 digit number with distinct non-zero digits as a secret number and players take turns 
    to guess their opponent's secret number. In each turn a player guesses a number and the 
    opponent should respond how many digits in the guessed number has matched with their secret 
    number in the form of Bulls and Cows. If the matching digits are in their right positions, 
    they are Bulls, if in different positions, they are Cows.

    For example:

    Secret number: 4271
    Opponent's try: 1234
    Answer: 1 bull and 2 cows
    (The bull is "2", the cows are "4" and "1".)\n""")


# Function checks if the number has 4 unique digits
def check_characters(number):
    if len(set(number)) == 4:
        return True
    else:
        return False


# Function to generate our number to guess for every play
def generate_num():
    while True:
        num = random.randint(1000, 9999)
        if check_characters(str(num)):
            return num


# Function to check if number of attempts is correct
def number_of_attempts():
    try:
        amount = int(input("\nGive the number of your attempts: "))
        if amount < 0:
            print("Number has to be bigger that 0.")
        return amount
    except ValueError:
        print("\nYou have to gave a number.")
        return 0


# Function to get correct number from the player
def extract_number():
    while True:
        # Check if it is a number
        try:
            number = int(input("\nGive the 4 digit number: "))
        except ValueError:
            print("\nYou can give only numbers.\n")
            continue

        #  Check if the number of digits is ok and if they are unique
        if len(str(number)) == 4:
            correctness = check_characters(str(number))
            if correctness == True:
                return number
            else:
                print("\nDigits cannot be repeated.")
                continue
        else:
            print("\nYou have to give 4 digit number.")


# Change a number to a list
def number_to_list(number):
    return [int(i) for i in str(number)]


# Main game function
def game():
    # Get the number to guess
    number_to_guess = generate_num()

    # Change the number to a list
    guess_list = number_to_list(number_to_guess)

    attempts = 0

    # Get how many attempts user wants to have
    while attempts <= 0:
        attempts = number_of_attempts()

    turn = 0

    while turn < attempts:
        # User guess the number
        number = extract_number()

        # Dictionary to storage score for this attempt
        cow_bull = {"COWS": 0, "BULLS": 0}

        # change number from user to a list
        number_list = number_to_list(number)

        # Compare elements in number_list and guess_list
        for i, j in zip(number_list, guess_list):

            # Look for common digit presence
            if j in number_list:

                # Common digit match and in wright position
                if j == i:
                    cow_bull["BULLS"] += 1

                # Common digit match but in wrong position
                else:
                    cow_bull["COWS"] += 1

        # Add current number and score to scores from previous attempts
        cows_and_bulls.update({number: cow_bull})

        # Check if player got 4 bulls
        if cow_bull["BULLS"] == 4:
            print("\nYou've won! The number was: ", number)
            break
        else:
            print("\nYou have: ")
            for key_number, score in cows_and_bulls.items():
                print("\nYour number: ", key_number)
                print("Your score:", score)

            print("\nYou have: ", attempts - turn - 1, "more attempts.")
            if turn == attempts - 1:
                print("\nYou've lost! The number was: ", number_to_guess)
            turn += 1


print("Hello at Cows and Bulls Game!")

while True:

    print("""\nMenu: 
    1 - show rules
    2 - start guessing
    3 - exit game \n""")

    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("\nYou can choose only numbers. Try again.\n")
        continue

    if choice == 1:
        game_rules()
    elif choice == 2:
        game()

        # Clearing the main score dictionary before next game
        cows_and_bulls.clear()
    elif choice == 3:
        print("\nBye bye!")
        break
    else:
        print("\nYou can choose only from 1 to 3. Try again.\n")
