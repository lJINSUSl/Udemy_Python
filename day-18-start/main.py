from turtle import Turtle, Screen, colormode
import random

colors = ['sky blue','lime green','red','black']

# tim = Turtle()
# tim.shape('arrow')
# tim.color('black')
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# screen = Screen()
# screen.exitonclick()

# tim2 = Turtle()
# tim2.shape('arrow')
#
# for _ in range(10):
#     tim2.dot(10)
#     tim2.penup()
#     tim2.forward(20)
#     tim2.pendown()
#
# screen = Screen()
# screen.exitonclick()
# tim3 = Turtle()


# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim3.forward(100)
#         tim3.right(angle)
# for n in range(3,11):
#     draw_shape(n)
#
# screen = Screen()
# screen.exitonclick()


# tim4 = Turtle()
# way_list = [1,2,3,4]
# while(1):
#     tim4.color(random.choice(colors))
#     if random.choice(way_list) == 1:
#         tim4.right(90)
#         tim4.forward(30)
#     elif random.choice(way_list) == 2:
#         tim4.left(90)
#         tim4.forward(30)
#     elif random.choice(way_list) == 3:
#         tim4.forward(30)
#     elif random.choice(way_list) == 4:
#         tim4.backward(30)
#
# screen = Screen()
# screen.exitonclick()



colormode(255)
# tim5 = Turtle()
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r,g,b
#
# directions = [0,90,180,270]
# tim5.pensize(15)
# tim5.speed('fastest')
#
# for _ in range(200):
#     tim5.color(random_color())
#     tim5.forward(30)
#     tim5.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()

# tim6 = Turtle()
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r,g,b
#
# tim6.hideturtle()
# tim6.speed('fastest')
# for _ in range(73):
#     tim6.color(random_color())
#     tim6.circle(100)
#     tim6.left(5)
#
#
# screen = Screen()
# screen.exitonclick()


import colorgram

tim7 = Turtle()


# colors = colorgram.extract('HIRST.jpg',30)
# list1 = []
# for _ in range(30):
#     r = colors[_].rgb.r
#     g = colors[_].rgb.g
#     b = colors[_].rgb.b
#     list1.append((r,g,b))
# print(list1)

color_list = [(248, 246, 236), (237, 250, 244), (251, 239, 248), (236, 243, 250), (233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174), (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155), (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43), (22, 179, 205), (11, 41, 23), (49, 126, 73), (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206), (133, 215, 229), (175, 177, 227), (59, 16, 31)]
tim7.speed('fastest')

for y in range(10):
    for x in range(10):
        tim7.color(random.choice(color_list))
        tim7.dot(20)
        tim7.penup()
        tim7.forward(50)
        tim7.pendown()
    tim7.penup()
    tim7.setx(0)
    tim7.sety(50*(y+1))


screen = Screen()
screen.exitonclick()