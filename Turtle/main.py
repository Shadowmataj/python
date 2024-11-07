import random
import turtle
from turtle import Turtle, Screen

import colorgram

'''
from turtle import *
import turtle
import turtle as t
'''
colors = ["royal blue", "SteelBlue", "teal", "peru", "peach puff", "dark orchid", "dark violet"]
angles = [90, 180, 270, 0]
turn = ["right", "left"]
timmy_the_turtle = Turtle()
turtle.colormode(255)
timmy_the_turtle.speed("fastest")
timmy_the_turtle.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color

def random_movement():
    timmy_the_turtle.pensize(10)
    for _ in range(100):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(30)
        timmy_the_turtle.setheading(random.choice(angles))

def circles(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

def extract_colors():
    image_colors = colorgram.extract("image.jpg", 15)
    list_of_colors = []
    for number in range(len(image_colors)):
        r = image_colors[number].rgb.r
        g = image_colors[number].rgb.g
        b = image_colors[number].rgb.b
        list_of_colors.append((r,g,b))
    return list_of_colors

def million_dollar_painting():
    colors_palette = extract_colors()
    timmy_the_turtle.penup()
    timmy_the_turtle.setheading(225)
    timmy_the_turtle.forward(300)
    timmy_the_turtle.setheading(0)
    timmy_the_turtle.hideturtle()
    for row in range(10):
        for column in range(10):
            timmy_the_turtle.dot(20, random.choice(colors_palette))
            timmy_the_turtle.forward(50)
        if row % 2 == 0:
            timmy_the_turtle.left(90)
            timmy_the_turtle.forward(50)
            timmy_the_turtle.left(90)
        else:
            timmy_the_turtle.right(90)
            timmy_the_turtle.forward(50)
            timmy_the_turtle.right(90)
        timmy_the_turtle.forward(50)
    timmy_the_turtle.showturtle()
    timmy_the_turtle.pendown()


mode = input("mode (random/circles/art): ").lower()
if mode == "random":
    random_movement()
elif mode == "circles":
    circles(5)
elif mode == "art":
    million_dollar_painting()


new_screen = Screen()
new_screen.exitonclick()
