from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

# tim = Turtle()
turtle_colors = ["brown", "blue", "green", "purple", "orange", "red"]


turtles = []

def draw_turtle():
    y_pos = 100
    for color in turtle_colors:
        t = Turtle()
        # t.speed(5)
        t.shape("turtle")
        t.penup()
        t.color(color)
        t.goto(-220, y_pos)
        y_pos -= 30
        turtles.append(t)

def run_race():
    race_on = True
    winner = ""
    while race_on:
        for turtle in turtles:
            turtle.forward(random.randint(1, 10))

        for turtle in turtles:
            if turtle.xcor() >= 220:
                race_on = False
                winner = turtle.pencolor()
    return winner

draw_turtle()
winner_color = run_race()

print(winner_color)
if winner_color == user_bet.lower():
    print(f"You win! The {winner_color} turtle is the winner.")
else:
    print(f"You lose! The {winner_color} turtle is the winner.")


screen.mainloop()