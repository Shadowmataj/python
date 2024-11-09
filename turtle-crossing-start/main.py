import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()

turtle = Player()

screen.onkey(turtle.move_up, "w")


game_is_on = True
counter = 0


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_a_new_car()
    car_manager.move()

    for car in car_manager.cars:
        car_left_limit = car.xcor() - 20
        car_right_limit = car.xcor() + 20

        car_bottom_position = car.ycor() - 15
        car_top_position = car.ycor() + 1

        if car_left_limit <= turtle.xcor() <= car_right_limit and  car_bottom_position <= turtle.ycor() <= car_top_position:
            scoreboard.game_over()
            game_is_on = not game_is_on


    if turtle.ycor() >= 270:
        turtle.reset()
        scoreboard.level_up()
        car_manager.speed_up()

screen.exitonclick()