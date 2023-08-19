from random import randint
def guessing_game():
     print("Random guessing game")
     user_LowerRange = int(input("what lower bound would you like? "))
     user_UpperRange = int(input("What upper bound would you like? "))
     random_number = randint(user_LowerRange,user_UpperRange)
     while True:
        user_input = int(input("Enter your guess "))
        if user_input > random_number:
            print("Too high")
            continue
        elif user_input < random_number:
            print("Too Low")
            continue
        elif user_input > user_UpperRange:
            print("Bruh")
            continue
        elif user_input < user_LowerRange:
            print("Bruh")
            continue
        else:
            user_input = random_number
            print("You guessed " + str(random_number) + " good job")
            break
guessing_game()
