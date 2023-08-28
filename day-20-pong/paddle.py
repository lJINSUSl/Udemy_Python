from turtle import Turtle

HEIGHT = 100
WIDTH = 20



class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.speed('fastest')

        self.penup()
        self.shape('square')
        self.color('white')


        self.shapesize(stretch_wid=5,stretch_len=1)
        self.setposition(position)



    def go_up(self):

        self.sety(self.ycor()+20)

    def go_down(self):

        self.sety(self.ycor()-20)
