from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        new_y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y_cor)

    def reset(self):
        self.setposition(STARTING_POSITION)