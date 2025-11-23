import turtle as t
import random


turture=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    return (r,g,b)


turture.speed("fastest")

def draw_spirograph(size_of_graph):
    for _ in range(int(360/size_of_graph)):
        turture.color(random_color())
        turture.circle(100)
        turture.setheading(turture.heading()+size_of_graph)

draw_spirograph(5)

screen=t.Screen()
screen.exitonclick()