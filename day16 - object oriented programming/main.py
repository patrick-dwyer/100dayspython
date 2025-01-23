# from turtle import Turtle, Screen

# #making turtle object
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('cyan2')
# timmy.forward(100)
# print(timmy)

# #look at screen object
# my_screen = Screen()
# my_screen.setup(10,10)
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'

print(table)


