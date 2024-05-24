from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 20, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            high_s = file.read()
        self.high_score = int(high_s)
        self.hideturtle()
        self.penup()
        self.color('white')
        self.teleport(0, 270)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", False, ALIGNMENT, FONT)
    def score_refresh(self):
        self.clear()
        self.score += 1
        self.score_update()
        # self.forward(20)
        # self.write(self.score, False,  "center", ("Arial", 8, "bold"))
        # self.back(20)
