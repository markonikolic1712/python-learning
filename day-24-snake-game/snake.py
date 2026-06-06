from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # glava se setuje na prvu poziciju

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg_num in self.segments:
            seg_num.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
            # zmija se krece tako sto se poslednji segment premesta na esto pretposlednjeg, pretposlednji na mesto ispred njea i tako sve dok se drugi segmen ne postavi na mestu prvog
            # prvi segment se pomera tamo gde ga korisnik posalje komandom a onda njega ostali segmenti prate
            # range(start=2, stop=0, step=-1)
            # for petlja je za pomeranje tela zmije a posle for petlje se sa .forward(MOVE_DISTANCE) pomeri glava. Nakon toga telo prati glavu i tako se zmija krece
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.head.setheading(RIGHT)