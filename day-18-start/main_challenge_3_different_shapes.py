from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
# ovako se odredjuje velicina prozora
# screen.setup(width=800, height=800)
# ovako se odredjuje velicina prozora u procentima u odnosu na velicinu monitora
# screen.setup(width=0.5, height=0.5)
# po defaultu velicina prozora koji se kreira je (width=0.5, height=0.75)
screen.setup(width=0.5, height=0.75)

t.shape("circle")

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "black"]
used_colors = []

for i in range(3, 10):
    t.setheading(0)
    new_color = random.choice(colors)

    while new_color in used_colors:
        print("Ponovo biram boju")
        new_color = random.choice(colors)

    used_colors.append(new_color)
    t.color(new_color)

    for s in range(0, i):
        t.forward(100)
        t.right(360.0/i)



screen.exitonclick()



