import random

playerMove=int(input("What Do You Choose?? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors\n"))
moves=[0,1,2]
ComputeMove=random.choice(moves)

rock=r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper=r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors=r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if playerMove==0:
    print("You Chose Rock")
    print(rock)
    if ComputeMove==0:
        print("Computer Chose Rock")
        print(rock)
        print("It's a Draw")
    elif ComputeMove==1:
        print("Computer Chose Paper")
        print(paper)
        print("You Lose.")
    else:
        print("Computer Chose Scissors")
        print(scissors)
        print("You Win!!!")
elif playerMove==1:
    print("You Chose Paper")
    print(paper)
    if ComputeMove==0:
        print("Computer Chose Rock")
        print(rock)
        print("You Win!!!")
    elif ComputeMove==1:
        print("Computer Chose Paper")
        print(paper)
        print("It's a Draw")
    else:
        print("Computer Chose Scissors")
        print(scissors)
        print("You Lose.")
elif playerMove==2:
    print("You Chose Scissors")
    print(scissors)
    if ComputeMove==0:
        print("Computer Chose Rock")
        print(rock)
        print("You Lose.")
    elif ComputeMove==1:
        print("Computer Chose Paper")
        print(paper)
        print("You Win!!!")
    else:
        print("Computer Chose Scissors")
        print(scissors)
        print("It's a Draw")
else:
    print("Invalid Option")