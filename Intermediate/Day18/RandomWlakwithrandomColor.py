import turtle as t
import random


turture=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    return (r,g,b)

directions=[0,90,180,270]
turture.pensize(15)
turture.speed("fastest")

for _ in range(200):
    turture.color(random_color())
    turture.forward(30)
    turture.setheading(random.choice(directions))

screen=t.Screen()
screen.exitonclick()