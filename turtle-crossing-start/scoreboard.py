from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 1
        self.goto(-260, 260)
        self.update_score()

    def update_score(self):
        self.write(arg=f'Level: {self.level}', move=False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write(arg=f'GAME OVER!', move=False, align="center", font=FONT)
