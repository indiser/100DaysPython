import turtle as t
import random

turture=t.Turtle()
furfure=t.Turtle()
gurgure=t.Turtle()

screen=t.Screen()
screen.setup(width=500,height=500)
user_bet=screen.textinput(title="Let's Go Gambling", prompt="Choose the color to bet on:").lower()

turture.shape("turtle")
furfure.shape("turtle")
gurgure.shape("turtle")

turture.color("red")
furfure.color("green")
gurgure.color("blue")

turture.penup()
furfure.penup()
gurgure.penup()

turture.goto(x=-230,y=-100)
furfure.goto(x=-230,y=30)
gurgure.goto(x=-230,y=150)

turture.speed("slowest")
furfure.speed("slowest")
gurgure.speed("slowest")

speed_list=[10,1,5]

is_race_on=True

while is_race_on:
    turture.forward(random.choice(speed_list))
    furfure.forward(random.choice(speed_list))
    gurgure.forward(random.choice(speed_list))
    
    if turture.xcor()>230:
        is_race_on=False
        if user_bet=="red":
            print("You won! Red turtle wins!")
        else:
            print("You lost! Red turtle wins!")
    elif furfure.xcor()>230:
        is_race_on=False
        if user_bet=="green":
            print("You won! Green turtle wins!")
        else:
            print("You lost! Green turtle wins!")
    elif gurgure.xcor()>230:
        is_race_on=False
        if user_bet=="blue":
            print("You won! Blue turtle wins!")
        else:
            print("You lost! Blue turtle wins!")

screen.exitonclick()