from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISHING_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.level = 1

    def go_forward(self):
        self.forward(MOVE_DISTANCE)

    def win(self):
        self.level += 1
        self.goto(STARTING_POSITION)
