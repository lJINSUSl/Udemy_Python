from turtle import Turtle
import random

COLORS = ['red','orange','yellow','green','blue','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):

        self.all_cars = []


    def create_car(self,location):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape('square')
        new_segment.speed('fastest')
        new_segment.color(random.choice(COLORS))
        new_segment.shapesize(1, 2)
        new_segment.goto(250, location)
        new_segment.setheading(180)
        self.all_cars.append(new_segment)

    def go_left(self,level):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE+(level-1)*MOVE_INCREMENT)

