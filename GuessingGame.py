import random

theNumber = random.randint(1, 100)

print("I am going to pick a number 0-100. It is your job to guess the number.")

guessList = []
playerGuess = input("Pick a number.")

while True:
    try:
        int(playerGuess)
        guessList.append(playerGuess)
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")
        playerGuess = input("Pick a number.")

if int(playerGuess) == theNumber:
    print("You've guessed the number!")
else:
    print("Hmm, that's not the number. Please try again!")
    playerGuess = input("Pick a number.")

while True:
    try:
        int(playerGuess)
        guessList.append(playerGuess)
        if int(playerGuess) == theNumber:
            print("You've guessed the number!")
            break
        elif abs(int(playerGuess) - theNumber) < abs(int(guessList[-2]) - theNumber):
            print("Warmer")
        elif abs(int(playerGuess) - theNumber) > abs(int(guessList[-2]) - theNumber):
            print("Colder")
        elif abs(int(playerGuess) - theNumber) == abs(int(guessList[-2]) - theNumber):
            print("Same Temp!")
        playerGuess = input("Pick a number.")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        playerGuess = input("Pick a number.")

print("You've won the game! The number is " + str(theNumber) + "!")