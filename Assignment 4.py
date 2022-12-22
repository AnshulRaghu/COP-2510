# Driver: Christian Taylor (U75799592), Navigator: Anshul Raghuvanshi (U69656337)
# This program is intended to play a series of games of rock, paper, scissor, lizard, spock with the user.
# We made a list of the 5 choices that are available.
# We made two functions:
#   the main() function intends to compare the user's entry to the computer's random choice from the list.
#   the end() function asks the user if they wanna play again. If yes, they play again. If no, the game summary is displayed.
# Finally, we used global variables and incremented them everytime the user won, lost, or tied the game against the computer.

import random

choices = ["rock", "paper", "scissors", "lizard", "spock"]
count = 0
win = 0
tie = 0
lost = 0

def end():
    while True:
        again = input("Do you want to keep playing? (yes/no): ").lower()
        if again == "yes":
            print("Great!")
            main()
        elif again == "no":
            print("Number of games played:", count)
            print("Games you won:", win)
            print("Games the computer won:", lost)
            print("Tie games:", tie)
            print("Thanks for playing!")
            exit()
        else:
            print("That's invalid. Please enter either yes or no.")

def main():
    while True:
        comp = random.choice(choices)
        global count
        global win
        global tie
        global lost
        x = input('Enter your choice: ')
        x = x.lower()
        if x == comp:
            print('Computer chose', comp)
            print('Tie!')
            count = count + 1
            tie = tie + 1
            end()
        elif x == "rock":
            print('Computer chose', comp)
            if comp == "paper":
                print("You lose!", comp, "covers", x)
                count = count + 1
                lost = lost + 1
                end()
            elif comp == "scissors":
                print("You win!", x, "crushes", comp)
                count = count + 1
                win = win + 1
                end()
            elif comp == "lizard":
                print("You win!", x, "crushes", comp)
                count = count + 1
                win = win + 1
                end()
            else:
                print("You lose!", comp, "vaporizes", x)
                count = count + 1
                lost = lost + 1
                end()
        elif x == "paper":
            print('Computer chose', comp)
            if comp == "rock":
                print("You win!", x, "covers", comp)
                count = count + 1
                win = win + 1
                end()
            elif comp == "scissors":
                print("You lose!", comp, "cuts", x)
                count = count + 1
                lost = lost + 1
                end()
            elif comp == "lizard":
                print("You lose!", comp, "eats", x)
                count = count + 1
                lost = lost + 1
                end()
            else:
                print("You win!", x, "disproves", comp)
                count = count + 1
                win = win + 1
                end()
        elif x == "scissors":
            print('Computer chose', comp)
            if comp == "rock":
                print("You lose!", comp, "crushes", x)
                count = count + 1
                lost = lost + 1
                end()
            elif comp == "paper":
                print("You win!", x, "cuts", comp)
                count = count + 1
                win = win + 1
                end()
            elif comp == "lizard":
                print("You win!", x, "decapitates", comp)
                count = count + 1
                win = win + 1
                end()
            else:
                print("You lose!", comp, "smashes", x)
                count = count + 1
                lost = lost + 1
                end()
        elif x == "lizard":
            print('Computer chose', comp)
            if comp == "rock":
                print("You lose!", comp, "crushes", x)
                count = count + 1
                lost = lost + 1
                end()
            elif comp == "paper":
                print("You win!", x, "eats", comp)
                count = count + 1
                win = win + 1
                end()
            elif comp == "scissors":
                print("You lose!", comp, "decapitates", x)
                count = count + 1
                lost = lost + 1
                end()
            else:
                print("You win!", x, "poisons", comp)
                count = count + 1
                win = win + 1
                end()
        elif x == "spock":
            print('Computer chose', comp)
            if comp == "rock":
                print("You win!", x, "vaporizes", comp)
                count = count + 1
                win = win + 1
                end()
            elif comp == "paper":
                print("You lose!", comp, "disproves", x)
                count = count + 1
                lost = lost + 1
                end()
            elif comp == "scissors":
                print("You win!", x, "smashes", comp)
                count = count + 1
                win = win + 1
                end()
            else:
                print("You lose!", comp, "poisons", x)
                count = count + 1
                lost = lost + 1
                end()
        else:
            print("That's invalid. Please enter Rock, Paper, Scissors, Lizard, or Spock: ")

print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
main()