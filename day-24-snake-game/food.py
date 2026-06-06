import random
from turtle import Turtle
import random

# food je krug koji se prikazuje u prozoru i kada zmija dodirne food on treba da nestane a da se naredni pojavi na random lokaciji
# ova klasa treba da ima funkcionalnost prikazivanja foor objekta na ekranu
# Food klasa nasledjue Turtle klasu i koristi njene metode
# koristi se self.shapesize(stretch_len=0.5, stretch_wid=0.5) da
class Food(Turtle):
    def __init__(self, ):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest") # setuje se fastest da se ne bi videla animacija kreiranja objekta
        # random lokacija - ide se od -280 do 280 da se food ne bi pojavio odmah uz ivicu jer bi igrac lako izgubio zivot
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)