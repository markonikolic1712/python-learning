from turtle import Turtle, Screen

t = Turtle()
t.shape("circle")
t.color("red")

pen_up = True
for _ in range(50):
    t.pendown() if pen_up else t.penup()
    t.forward(10)
    pen_up = not pen_up









screen = Screen()
# ako ne pozovemo metodu exitonclick() ekran ce se pojaviti i odmah zatvoriti
# poziv metode exitonclick() mora da bude na kraju koda inace se nista nece iscrtati na ekranu
screen.exitonclick()



