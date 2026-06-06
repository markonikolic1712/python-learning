import colorgram

# za izvlacenje boja zi slike image.jpg koristi se paket colorgram.py
# colors = colorgram.extract('image.jpg', 100)
#
# rgb_colors = []
#
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
# rgb_colors.clear()


import turtle as turtle_package
import random

t = turtle_package.Turtle()
screen = turtle_package.Screen()

turtle_package.colormode(255)
t.speed("fastest")

# u rgb_colors je lista boja koje je program izvukao iz image.jpg
# iz ove liste sam izbrisao boje koje je program pokupio a koja je pozadina. Kada sem to izbacio ostala mi je ova dole lista i nju cuvam u rgb_colors
# nakon ovoga ovaj kod gore moze da se zakomentarise
rgb_colors = [(249, 229, 236), (240, 250, 244), (29, 41, 60), (49, 92, 143), (145, 81, 44), (170, 14, 28), (160, 56, 87), (227, 154, 8), (209, 162, 105), (235, 217, 75), (66, 30, 43), (236, 240, 246), (37, 142, 47), (222, 225, 4), (48, 36, 30), (46, 47, 96), (95, 193, 168), (120, 161, 172), (19, 54, 47), (243, 89, 22), (161, 16, 13), (18, 97, 45), (212, 58, 79), (49, 169, 80), (189, 146, 159), (231, 173, 186), (226, 177, 168), (45, 153, 195), (160, 212, 184), (74, 77, 43), (116, 122, 156), (20, 74, 105), (184, 189, 203)]

# t.shape("circle")
# t.pensize(10)

rows = 10
columns = 10
radius = 20
space = 50

t.penup()
t.hideturtle()

t.goto(-250, -200)

for _ in range(rows):
    t.setheading(0)

    for _ in range(columns):
        t.dot(radius, random.choice(rgb_colors))
        t.forward(radius + space)

    t.setheading(90)
    t.forward(radius + space)
    t.setheading(180)
    t.forward(rows * radius + columns * space)




screen.exitonclick()