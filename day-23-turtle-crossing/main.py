import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars[:]:
        # detekcija kolizije automobila i kornjace
        #if car.distance(player) < 20:
        # ovo je preciznija detekcija kolizije
        if (abs(car.xcor() - player.xcor()) < 30 and
                abs(car.ycor() - player.ycor()) < 20):
            game_is_on = False
            scoreboard.game_over()

        # kada car objekat predje preko leve ivice ekrana (izadje izvan ekrana) brise se iz niza all_cars
        if car.xcor() < -300:
            car.clear()
            car.hideturtle()
            car_manager.all_cars.remove(car)

    # provera da li je player dosao do finisa
    # ako jeste vracamo ga na startnu poziciju i ubrzavamo automobile
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()
