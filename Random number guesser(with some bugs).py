import random
from tkinter import TRUE

first = int(input("Where would you like to start: "))

last = int(input("Up to what number: "))

randomlist = []

for i in range(0,0):
    n = random.randint(first, last)
    randomlist.append(n)

def main():
    guess = int(input("what's your guess? "))
    if guess != randomlist: 
            print("try again")
            return True
    elif guess == randomlist:
            print("Good job")
            return False

while True:
    while main() == True:
        guess = int(input("What's your guess?: "))
        break

    print("Good Job")
    retry = input("Would you like to play again (y/n)?: ")

    if retry == "y":
        True

    if retry == "n":
        print("I didn't want to play anyway baka")
        break

    if retry != ("y" , "n"):
        print("Only 'y' or 'n' please")


        
 



        



