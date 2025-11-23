import blacjack_art
import random

blacjack_art.logo()

def list_sum(list1):
    sum=0
    for i in list1:
        sum+=i
    while sum > 21 and 11 in list1:
        list1[list1.index(11)] = 1
        sum = 0
        for i in list1:
            sum+=i
    return sum

def win_condition(sum1,sum2):
    sub1=21-sum1
    sub2=21-sum2
    if sub1 < sub2:
        return True
    else:
        return False

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
playerHand=[]
dealerHand=[]


for i in range(2):
    playerHand.append(random.choice(cards))
    dealerHand.append(random.choice(cards))
dealerSecondcard=dealerHand.pop()

while True:
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print(f"Players Hands Are:{playerHand}\n")
    print(f"Your Total card number is:{list_sum(playerHand)}\n")
    print(f"Dealers Hands Are:{dealerHand} [Hidden Card]\n")
    print(f"Dealers Total card number is:{list_sum(dealerHand)}\n")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

    user_choice=input('Do you want to "Hit" to add anothercard to your hand or "Stand" to stick with your hand?\n').lower()
    if user_choice not in ["hit","stand"]:
        print("Invalid Input")
        continue
    if user_choice=="hit":
        playerHand.append(random.choice(cards))
        if list_sum(playerHand) > 21:
            print(f"Your cards were:{playerHand}")
            print(f"Your Total card number was {list_sum(playerHand)}")
            print("Dealer Won....")
            break
        continue
    else:
        dealerHand.append(dealerSecondcard)
        while list_sum(dealerHand) < 17:
            dealerHand.append(random.choice(cards))
            if list_sum(dealerHand) > 21:
                print(f"Your cards were:{playerHand}")
                print(f"Your Total card number was {list_sum(playerHand)}")
                print(f"Dealers cards were:{dealerHand}")
                print(f"Dealers Total card number was {list_sum(dealerHand)}")
                print("You Win....")
                break
        if list_sum(playerHand)==21:
            print(f"Your Cards are:{playerHand}")
            print(f"Your Total Card number is:{list_sum(playerHand)}.")
            print("You Won....")
            break
        if list_sum(dealerHand)==21:
            print(f"Dealer Cards are:{dealerHand}")
            print(f"Dealers Total Card Sum is:{list_sum(dealerHand)}.")
            print("Dealer Won..")
            break
        if list_sum(playerHand)==list_sum(dealerHand):
            print(f"Your Cards are:{playerHand}")
            print(f"Your Total Card number is {list_sum(playerHand)}.")
            print(f"Dealers Cards are:{dealerHand}")
            print(f"Dealers Total Card number is {list_sum(dealerHand)}.")
            print("Push")
            break
        if list_sum(dealerHand) < 21:
            if win_condition(list_sum(playerHand),list_sum(dealerHand)):
                print(f"Your Cards are:{playerHand}")
                print(f"Your Total card Sum was:{list_sum(playerHand)}")
                print(f"Dealers Cards are:{dealerHand}")
                print(f"Dealers Total card Sum was:{list_sum(dealerHand)}")
                print("You were closer to 21")
                print("You Won.....")
                break
            else:
                print(f"Your Cards are:{playerHand}")
                print(f"Your Total card Sum was:{list_sum(playerHand)}")
                print(f"Dealers Cards are:{dealerHand}")
                print(f"Dealers Total card Sum was:{list_sum(dealerHand)}")
                print("Dealer was closer to 21")
                print("Dealer won...")
        break

