from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
MAX_TOP = 260
POSITIONS = {
    "right": 40,
    "left": -40
}

INVERTED_POSITIONS = {
    "left": "right",
    "right": "left"
}


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = {
            "right": 0,
            "left": 0
        }
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard("left")
        self.update_scoreboard("right")

    def increase_scoreboard(self, side):
        self.scores[side] += 1
        self.clear()
        self.update_scoreboard(side)
        self.update_scoreboard(INVERTED_POSITIONS[side])

    def update_scoreboard(self, side):
        self.goto(POSITIONS[side],MAX_TOP)
        self.write(arg=f"{self.scores[side]}", align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        self.goto(0, 0)

        if player == "left":
            player_number = 1
        else:
            player_number =2
        self.write(arg=f"PLAYER {player_number} WINS!", align=ALIGNMENT, font=FONT)