from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_left():
    tim.setheading(tim.heading() + 15)
    tim.tilt()
    
    print(tim.heading())

def rotate_right():
    tim.setheading(tim.heading() - 15)
    tim.tilt(-15)
    
    

def clear_center():
    tim.reset()

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear_center)

screen.exitonclick()