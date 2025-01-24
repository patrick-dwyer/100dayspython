from turtle import Turtle, Screen
from random import randrange, choice

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

# #challenge 1: draw  square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# #challenge 2: draw dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()

screen = Screen()
screen.colormode(255)
# #challenge 4: polygons of random colours
# for i in range(3,11):
#     angle = 360/i
#     timmy.color(randrange(0,255), randrange(0,255), randrange(0,255))
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(angle)

#challenge 5: random walk
i = 0
timmy.width(10)
timmy.speed(6)
while i != 1:
    angles = [0, 90, 180, 270]
    timmy.rt(choice(angles))
    timmy.color(randrange(0,255), randrange(0,255), randrange(0,255))
    timmy.fd(100)
    print(choice(angles))

screen.exitonclick()

