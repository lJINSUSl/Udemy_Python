from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title= "Make you bet",prompt= "Who will win? Choose from rainbow: ")
colors = ['red','orange','yellow','green','blue','purple']
all_turtles = []

if user_bet:
    is_race_on = True


for color in range(len(colors)):
    tim = Turtle(shape= 'turtle')
    tim.color(colors[color])
    tim.penup()
    tim.goto(x=-230,y=-80+color*40)
    all_turtles.append(tim)

while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor() >= 230:
            is_race_on = False

            winning_color = turtles.pencolor()

            if winning_color == turtles:
                print(f"The winner is {winning_color}. You've won")
            else:
                print(f"The winner is {winning_color}. You've lost")
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)

screen.exitonclick()