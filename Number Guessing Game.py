#Importing required modules for the program
import random
import math

#Creating a function that error handles when user inputs a number for the game
def number_input(message):
    while True:
        try:
            number = int(input(message))
            if number <= 0:
                print("Game only works with positive numbers!")
                continue
        except ValueError:
            print("Please enter a number (without decimals)!")
        else:
            return number


def game(lower, upper): #Main game functionality code
    while True:
        #Validating if the global variables set initially are still none
        #If so, you can't continue a game
        if lower == 0 or upper == 0:
            print("No range set yet! \nStart a new game!")
            break
        else:
            #Generating a random number for user to guess
            random_number = random.randint(lower, upper)

            #Now let's get into the game!

            #Initializing number of guesses
            guess_count = 0
            #Setting minimum amount of guesses according to the range
            min_guesses = round(math.log(upper - (lower + 1), 2))
            print(f"\nYou have only {min_guesses} guesses. \nGood Luck!")

            while True:
                user_input = number_input("\nEnter your guess: ")
                if user_input < lower or user_input > upper:
                    print("Your guess is out of the range!")
                elif user_input < random_number or user_input > random_number:
                    guess_count += 1
                    if user_input < random_number: 
                        print("I would aim higher if I were you...")
                    elif user_input > random_number:
                        print("Miss.. going lower will help...")
                    guesses_left = min_guesses - guess_count
                    print(f'Number of guesses left = {guesses_left}')
                    if guesses_left == 0:
                        print("You lost :( Better luck next time!")
                        break
                else:
                    print("Guess was correct!")
                    print(f"You did it in {guess_count} out of {min_guesses} guesses. Well Done!")
                    break
            break


def main_menu(): #Creating a main menu for options in the game
    lower, upper = 0, 0
    #Messages at the beginning of the game
    print("---The Number Guessing Game---")
    print("Welcome to the number guessing game!")
    #Messages loaded when continuing the game on repeat
    while True:
        if lower == 0 or upper == 0:
            print("\nWhat would you like to do? \nEnter the respective index on the left\n")
        else:
            print("\nFancy another go? \nEnter the respective index on the left\n")
        print("1. New Game with New Range")
        print("2. Continue Game with Same Range")
        print("3. Exit Game\n")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid Input!")
            continue
        if choice == 1:
            #Starting a new game
            print("To setup game, enter preferred number range\n")
            #Prompting user to input a number each to generate a number range to set a number to guess
            lower = number_input("Enter the lowest number of your range: ")
            upper = number_input("Enter the highest number of your range: ")
            game(lower, upper)
        elif choice == 2:
            #Continuing an already number range set game
            game(lower, upper)
        elif choice == 3:
            print("Exiting Game. GoodBye!")
            break
        else:
            print("Invalid Index!")

if __name__ == '__main__':
    main_menu()
