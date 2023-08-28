from turtle import Turtle

LOCATION = (300,200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()

    def reset_score(self):
        self.clear()
        self.goto(LOCATION)
        self.write(f"Score : {self.score}", align='center')
        self.score += 1