import turtle
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
# iskljucuje se tracer da bi mogao da se koristi update()
# svaki put kada pormenimo poziciju elementa na ekranu treba da se pozove update() sa osvezi prikaz
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard(SCREEN_WIDTH)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    # screen.update() mora da bude izvan for petlje jer zelimo da prvo pomerimo sve elemente pa da tek onda osvezimo ekran
    screen.update()
    time.sleep(0.15)
    snake.move()

    # detekcija kontakta zmije i food-a
    if snake.head.distance(food) < 15:
        print("KONTAKT")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detekcija kolizije zmije i zida
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("GAME OVER")
        game_is_on = False
        scoreboard.game_over()

    # detekcija kolizije zmije i repa
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print("GAME OVER")
            game_is_on = False
            scoreboard.game_over()

#screen.mainloop()
screen.exitonclick()

























screen.exitonclick()
