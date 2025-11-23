from turtle import Turtle
import random


colors_list=["red","yellow","green","blue"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.color(random.choice(colors_list))
        self.penup()
        self.goto(300,0)
        self.speed("slowest")

    def move_forward(self):
        self.backward(STARTING_MOVE_DISTANCE)