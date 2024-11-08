import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.pensize(20)
        self.direction = 0
        self.right_directions = []
        self.right_directions.extend(list(range(20, 46)))
        self.right_directions.extend(list(range(125, 161)))
        self.right_directions.extend(list(range(200, 226)))
        self.right_directions.extend(list(range(315, 336)))
        self.move_speed = 0.01
        self.start_heading()

    def start_heading(self):
        self.direction = 0
        self.direction = random.choice(self.right_directions)

    def game(self):
        self.setheading(self.direction)
        self.forward(2)
        self.setheading(0)

    def change_direction(self):
            self.direction *= -1

    def paddle_collision(self):
            self.direction -= 180
            self.direction *= -1
            self.move_speed *= 0.8

    def reset(self):
        self.hideturtle()
        self.setposition(0,0)
        self.move_speed = 0.01
        self.start_heading()
        self.showturtle()
