from turtle import Turtle

STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE_Y=280


class Turture(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.speed("fast")

    def go_forward(self):
        self.forward(10)
    def go_backwrd(self):
        self.backward(10)
    def go_left(self):
        new_x=self.xcor()-10
        self.goto(new_x,self.ycor())
    def go_right(self):
        new_x=self.xcor()+10
        self.goto(new_x,self.ycor())