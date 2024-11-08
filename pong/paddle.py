from turtle import Turtle
STARTING_POSITIONS = {
    "right": (470, 0),
    "left": (-470, 0)
}

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(STARTING_POSITIONS[side])
        self.side = side

    def up(self):
        if self.ycor() < 250:
            y_position = self.ycor() + 20
            x_position = self.xcor()
            self.setposition(x_position, y_position)

    def down(self):
        if self.ycor() > -250:
            y_position = self.ycor() - 20
            x_position = self.xcor()
            self.setposition(x_position, y_position)

    def reset(self, side):
        self.hideturtle()
        self.goto(STARTING_POSITIONS[side])
        self.showturtle()
