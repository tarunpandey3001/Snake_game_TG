import random
import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEPS_TO_MOVE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, position):
        tur = t.Turtle()
        # tur.speed('slow')
        tur.shape('square')
        tur.penup()
        tur.goto(position)
        tur.color('white')
        self.all_turtles.append(tur)

    def reset(self):
        for seg in self.all_turtles:
            seg.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def move_forward(self):
        for i in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[i - 1].xcor()
            new_y = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].goto(new_x, new_y)
        self.all_turtles[0].forward(STEPS_TO_MOVE)

    def left(self):
        if self.all_turtles[0].heading() != RIGHT:
            self.all_turtles[0].setheading(LEFT)

    def right(self):
        if self.all_turtles[0].heading() != LEFT:
            self.all_turtles[0].setheading(RIGHT)

    def up(self):
        if self.all_turtles[0].heading() != DOWN:
            self.all_turtles[0].seth(UP)

    def down(self):
        if self.all_turtles[0].heading() != UP:
            self.all_turtles[0].seth(DOWN)



