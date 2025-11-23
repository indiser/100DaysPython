from turtle import Turtle, Screen

turture=Turtle()

turture.shape("turtle")
turture.color("red")

for i in range(0,4):
    turture.forward(100)
    turture.right(90)



screen=Screen()
screen.exitonclick()