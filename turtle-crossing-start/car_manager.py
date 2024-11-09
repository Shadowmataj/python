import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_a_new_car(self):
        random_chance = random.randint(1,40)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(350, random.randint(-250,250))
            self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT