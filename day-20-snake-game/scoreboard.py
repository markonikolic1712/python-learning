from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self, SCREEN_WIDTH):
        super().__init__()
        self.score = 0
        self.screen_width = SCREEN_WIDTH
        self.color("white")
        self.penup()
        self.goto(0, self.screen_width // 2 - 25)
        self.update_scoreboard()
        self.hideturtle()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        print(self.score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


