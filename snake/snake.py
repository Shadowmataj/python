from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body_part = Turtle(shape="square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.segments.append(body_part)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for part_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[part_number - 1].xcor()
            new_y = self.segments[part_number - 1].ycor()
            self.segments[part_number].goto(new_x, new_y)
        self.segments[0].forward(20)
