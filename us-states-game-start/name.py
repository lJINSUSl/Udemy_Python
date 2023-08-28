from turtle import Turtle

class Name(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def city_write(self,city,coordinate):
        self.goto(coordinate)
        self.write(city)
