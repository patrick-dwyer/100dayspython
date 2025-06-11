import colorgram
from turtle import Turtle, Screen
from random import randrange, choice

colors = colorgram.extract('dhs3823_0_1280_0-768x719.jpg', 30)

color_list = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b

    color_list.append((r, g, b))


timmy = Turtle()
timmy.shape('turtle')
timmy.color('black')

screen = Screen()
screen.colormode(255)

timmy.dot(50)

screen.exitonclick()
# for row in range(10):
    # timmy.dot(50, colors(randrange(0, 30, 1)))