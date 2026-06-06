from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_WIDTH_LIMIT = SCREEN_WIDTH / 2 - 75
# PADDLE_SPEED = 10
PADDLE_SPEED = 30
BALL_SPEED = 6

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
# sa screen.tracer(0) iskljucujemo animacije da se ne bi videlo kreiranje objekata na pocetnom ekranu
# kada se sa tracer iskljuce animacije nista se nece videti na ekranu pa zato mora da se poziva update() metoda u while petlji i ona manuelno radi update i refresh ekrana
screen.tracer(0)

r_paddle = Paddle((350, 0), PADDLE_SPEED, SCREEN_HEIGHT)
l_paddle = Paddle((-350, 0), PADDLE_SPEED, SCREEN_HEIGHT)

screen.listen()
# PALYER 1 - koristi strelica gore i dole
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# PLAYER 2 - koristi w za gore i s za dole
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball(BALL_SPEED, SCREEN_HEIGHT)
ball_direction = "up_right"
# ball_direction = "down_right"

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update() # mora update() zato sto smo gore koristi screen.tracer(0)
    ball.move()

    # r_paddle.move()
    # l_paddle.move()

    # provera da li je paddle dosao do vrha ili dna ekrana - kada dodje do vrha ili dna treba da stane
    if r_paddle.ycor() > (SCREEN_HEIGHT / 2 - 55) or (r_paddle.ycor() < -1 * (SCREEN_HEIGHT / 2 - 65)):
        r_paddle.direction = 0
    if l_paddle.ycor() > (SCREEN_HEIGHT / 2 - 55) or (l_paddle.ycor() < -1 * (SCREEN_HEIGHT / 2 - 65)):
        l_paddle.direction = 0


    # detektovanje kolizije lopte i gornje ili donje ivice
    if ball.ycor() > (SCREEN_HEIGHT / 2) - 15 or ball.ycor() < -1 * (SCREEN_HEIGHT / 2) + 20:
        ball.bounce_y()

    # detektovanje kolizije lopte i paddel-a
    if (ball.distance(r_paddle) < 50 and ball.xcor() >= SCREEN_WIDTH_LIMIT) or (ball.distance(l_paddle) < 50 and ball.xcor() <= -1 * SCREEN_WIDTH_LIMIT):
        ball.bounce_x()

    # detekcija kada je r_paddle igrac promasio loptu
    if ball.xcor() > SCREEN_WIDTH_LIMIT + 100:
        ball.reset_position()
        scoreboard.l_point()

    # detekcija kada je l_paddle igrac promasio loptu
    if ball.xcor() < -1 * (SCREEN_WIDTH_LIMIT + 100):
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()





