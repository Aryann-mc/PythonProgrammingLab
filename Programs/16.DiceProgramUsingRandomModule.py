#Dice program using random module
import random
while True:
    choice = input("Welcome to dice game press Y to start and N to stop: ")
    if choice == "Y" or choice == "y":
        roll = random.randint(1, 6)
        print("You rolled a ", roll)
    else:
        print("Goodbye!")
        break

