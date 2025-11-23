import random
import numberguess_art

numberguess_art.logo()

computer_number = random.randint(1, 100)

def easy_option(computerNumber):
    easy=10
    print(f"You have {easy} options left")
    while easy != 0:
        userInput=int(input("Enter the choice:\n"))
        if easy==0:
            print("You are Out of options")
            break
        if userInput > computerNumber:
            print("Too High")
            easy-=1
            print(f"You have {easy} options left")
            print("Guess again.")
        elif userInput < computerNumber:
            print("Too Low")
            easy-=1
            print(f"You have {easy} options left")
            print("Guess again.")
        else:
            print(f"Yes the computer's number was:{computerNumber}")
            print("You win")
            break
        

def hard_option(computerNumber):
    hard=5
    print(f"You have {hard} options left")
    while hard != 0:
        userInput=int(input("Enter the choice:\n"))
        if hard==0:
            print("You are Out of options")
            break
        if userInput > computerNumber:
            print("Too High")
            hard-=1
            print(f"You have {hard} options left")
            print("Guess again.")
        elif userInput < computerNumber:
            print("Too Low")
            hard-=1
            print(f"You have {hard} options left")
            print("Guess again.")
        else:
            print(f"Yes the computer's number was:{computerNumber}")
            print("You win")
            break
        


print('Welcome to the number guesser..')
print("The Computer has a number between 1-100")
options=input('Type "Easy" fo easy mode or "Hard" for hard mode:\n').lower()


if options=="easy":
    easy_option(computer_number)
elif options=="hard":
    hard_option(computer_number)
else:
    print("Invalid Option")


