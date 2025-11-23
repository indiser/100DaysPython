from  turtle import Turtle, Screen
import random


t=Turtle()

colors=["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

def draw_shapes(num_sides):
    degrees=360/num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(degrees)

for i in range(3,11):
    t.color(colors[i-3])
    draw_shapes(i)

screen=Screen()
screen.exitonclick()