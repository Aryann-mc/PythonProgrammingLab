#Number guessing game
import random
secret=random.randint(1,20)
attempts=0
while attempts<5:
    guess=int(input("Welcome to number guessing game\nGuess the number: "))
    attempts+=1
    if guess==secret:
        print("You guessed the number")
        break
    elif guess<secret:
        print("Too low")
    else:
        print("Too high")
if guess!=secret:
    print("You guessed the wrong number")