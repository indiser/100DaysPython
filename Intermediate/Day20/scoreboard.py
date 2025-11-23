from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("highscore.txt") as filp:
            self.high_score=int(filp.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=ALIGNMENT,font=FONT)


    def increseScore(self):
        self.score+=1
        self.updateScore()

    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align=ALIGNMENT,font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        with open("highscore.txt","w") as filp:
            filp.write(str(self.high_score))
        self.score=0
        self.updateScore()