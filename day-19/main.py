from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# kazemo screen objektu d apocne da slusa akcije korisnika
screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_screen, key="c")


# sa mainloop() ekran se zatvara samo kada kliknem na X a ne i kada kliknem negde u prozoru
screen.mainloop()

