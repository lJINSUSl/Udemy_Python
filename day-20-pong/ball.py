from turtle import Turtle
import random
STARTING_DIRECTION = random.randint(0,360)
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('circle')
        self.color('white')
        self.setheading(STARTING_DIRECTION)
        self.new_direction = STARTING_DIRECTION


    def move(self,stack):
        self.forward(10+stack)

        if self.ycor() > 280 or self.ycor() < -280:
            self.new_direction = 360-self.new_direction
            self.setheading(self.new_direction)



    def bounce_with_pad(self):
        self.new_direction = 90+ self.new_direction
        self.setheading(self.new_direction)
        self.forward(10)

    def go_out(self):
        self.goto(0,0)
        self.new_direction = random.randint(0,360)
        self.setheading(self.new_direction)

