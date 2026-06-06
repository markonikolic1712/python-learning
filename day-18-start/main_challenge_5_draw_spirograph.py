import turtle as turtle_package
import random

t = turtle_package.Turtle()
screen = turtle_package.Screen()
# ovako se odredjuje velicina prozora
# screen.setup(width=800, height=800)
# ovako se odredjuje velicina prozora u procentima u odnosu na velicinu monitora
# screen.setup(width=0.5, height=0.5)
# po defaultu velicina prozora koji se kreira je (width=0.5, height=0.75)
screen.setup(width=0.5, height=0.75)

# da bi za setovanje boje mogli da koristimo rgb() turtle modul mora da se promeni sa colormode
turtle_package.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# t.shape("circle")
#t.pensize(10)
t.speed("fastest")

def draw_spirograph(gap):
    for i in range(0, 360, gap):
        t.setheading(i)
        t.color(random_color())
        t.circle(100)
        print(f"crtam krug sa orjentacinom: {i}")

draw_spirograph(5)


screen.exitonclick()



