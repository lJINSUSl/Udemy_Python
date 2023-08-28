# import turtle
#
#
#
#
# #timmy라는 객체(object) 에 turtle 모듈에서 불러온 Turtle 클래스를 저장함.
# timmy = turtle.Turtle()

#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('red','green')
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
print(table)

table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
table.align = 'l'

print(table)