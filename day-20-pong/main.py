import time
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.title('ping-pong')
screen.setup(width= 800,height=600)
screen.bgcolor('black')
screen.tracer(0)

pad1 = Paddle((350,0))

pad2 = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(pad1.go_up,"Up")
screen.onkey(pad1.go_down, "Down")
screen.onkey(pad2.go_up, "w")
screen.onkey(pad2.go_down, "s")
stack = 0
game_is_on = True

while game_is_on:

    time.sleep(0.05)
    ball.move(stack)
    if (ball.distance(pad1) < 50 and ball.xcor() > 330) or (ball.distance(pad2) < 50 and ball.xcor() < -330) :
        ball.bounce_with_pad()
    if  ball.xcor()<-360:
        ball.go_out()
        scoreboard.r_point()
        stack+=5
    if  ball.xcor() > 360:
        ball.go_out()
        scoreboard.l_point()
        stack += 5
    screen.update()



screen.exitonclick()