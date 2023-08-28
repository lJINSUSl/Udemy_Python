from turtle import Turtle, Screen
import time
import random
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(600,600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

time_car = 0
segments = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkey(player.go_forward,"Up")
    time_car += 1
    if time_car%6 ==0:
        LOCATION = random.randint(-250, 250)
        car_manager.create_car(LOCATION)
    car_manager.go_left(level=player.level)
    scoreboard.score(player.level)


    #collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #win
    if player.ycor() > 280:

        player.win()
        scoreboard.clear()








screen.exitonclick()
