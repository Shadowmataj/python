from time import sleep
from turtle import Screen

from net import Net
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

MAX_TOP = 280
MAX_BOTTOM = -280

screen = Screen()
screen.title("PONG")
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

def reset ():
    ball.reset()
    left_paddle.reset("left")
    right_paddle.reset("right")

def pong():

    game_is_on = True
    while game_is_on:
        screen.update()
        sleep(ball.move_speed)
        ball.game()
        for paddle in paddles:
            if ball.distance(paddle) < 50 and (ball.xcor() < -450 or ball.xcor() > 450):
                ball.paddle_collision()

        if ball.ycor() >= MAX_TOP or ball.ycor() <= MAX_BOTTOM:
            ball.change_direction()

        if ball.xcor() > 500:
            scoreboard.increase_scoreboard("left")
            reset()
            game_is_on = not game_is_on
            screen.update()

        if ball.xcor() < -500:
            scoreboard.increase_scoreboard("right")
            reset()
            game_is_on = not game_is_on
            screen.update()

        for player in scoreboard.scores:
            if scoreboard.scores[player] == 10:
                game_is_on = not game_is_on
                scoreboard.game_over(player)
                screen.update()





net = Net(screen.window_height())
scoreboard = Scoreboard()
ball = Ball()
left_paddle = Paddle("left")
right_paddle = Paddle("right")

paddles = [right_paddle, left_paddle]
screen.update()


screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkey(pong, "space")

screen.exitonclick()
