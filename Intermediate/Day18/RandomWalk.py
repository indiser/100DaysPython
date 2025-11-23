from  turtle import Turtle, Screen
import random


t=Turtle()

colors=["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
directions=[0,90,180,270]
t.pensize(15)
t.speed("fastest")

for _ in range(200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))

screen=Screen()
screen.exitonclick()