import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEPS_TO_MOVE = 20


class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            tur = t.Turtle()
            # tur.speed('slow')
            tur.shape('square')
            tur.penup()
            tur.goto(positions)
            tur.color('white')
            self.all_turtles.append(tur)

    def move_forward(self):
        # n = 3
        # all_turtles = []

        for i in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[i - 1].xcor()
            new_y = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].setposition(new_x, new_y)
        self.all_turtles[0].forward(STEPS_TO_MOVE)
