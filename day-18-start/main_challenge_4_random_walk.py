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
t.pensize(10)
t.speed(0.5)


colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "black"]
headings = [0, 90, 180, 270]

for i in range(3, 200):
    t.setheading(0)
    color = random.choice(colors)
    t.color(color)
    t.setheading(random.choice(headings))
    t.forward(50)




screen.exitonclick()



