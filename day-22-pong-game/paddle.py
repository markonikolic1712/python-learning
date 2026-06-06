from turtle import Turtle, Screen

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position, paddle_speed, screen_height):
        super().__init__()
        self.paddle_speed = paddle_speed
        self.penup()
        self.goto(position[0], position[1])
        # self.speed("fastest")  # setuje se fastest da se ne bi videla animacija kreiranja objekta
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.direction = 0
        self.screen_height = screen_height

    def up(self):
        self.direction = UP
        self.move()

    def down(self):
        self.direction = DOWN
        self.move()

    def move(self):
        # time.sleep(0.01)
        if self.direction == UP and self.ycor() < (self.screen_height / 2 - 55):
            self.sety(self.ycor() + self.paddle_speed)
        elif self.direction == DOWN and self.ycor() > -1 * (self.screen_height / 2 - 65):
            self.sety(self.ycor() - self.paddle_speed)






