import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win th race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_position = -240
y_position = -100
color_selection = 0
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x_position, y=y_position)
    y_position += 50
    color_selection +=1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 220:
            is_race_on = False
            winner_color = tur.pencolor()
            if user_bet == winner_color:
                print(f"You've won, the {winner_color} turtle is the winner!")
            else:
                print(f"You've lost the bet, the {winner_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        tur.forward(rand_distance)
screen.exitonclick()
