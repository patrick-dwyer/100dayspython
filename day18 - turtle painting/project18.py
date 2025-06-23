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

#get rid of white dot colors
color_list = color_list[4:]

timmy = Turtle()
timmy.shape('turtle')
timmy.pu()
timmy.speed(0)
timmy.hideturtle()

screen = Screen()
screen.colormode(255)

for i in range(10): 

    for k in range(10):
        colour = choice(color_list)
        r,g,b = colour[0], colour[1], colour[2]
        timmy.fd(50)
        timmy.dot(20, (r,g,b))

    timmy.setx(0)
    
    timmy.sety(timmy.position()[1] + 25)

screen.exitonclick()
# for row in range(10):
    # timmy.dot(50, colors(randrange(0, 30, 1)))