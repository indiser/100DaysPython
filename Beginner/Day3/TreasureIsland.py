import time

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome To Treasure Island")
print("Your Mission is to find the treasure....")

leftRight=input("Which Direction Do You Choose?? Left Or Right\n").lower()
if leftRight=="left":
    swimWait=input("What Do You Want To Do Next?? Swim or Wait\n").lower()
    if swimWait=="wait":
        time.sleep(5)
        redBlueYellow=input("Which Door Do You want to go through?? Red , Blue or Yellow\n").lower()
        if redBlueYellow=="yellow":
            print("You Win!!!")
        elif redBlueYellow=="red":
            print("Burned By Fire. Game Over")
        elif redBlueYellow=="blue":
            print("Eaten By Beasts. Game Over")
    elif swimWait=="swim":
        print("Attacked By Trout. Game Over")
    else:
        print("Attacked By Trout. Game Over")
elif leftRight=="right":
    print("Fall into a hole. Game Over")
else:
    print("Fall into a hole. Game Over")
