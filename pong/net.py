from turtle import Turtle


class Net(Turtle):
    def __init__(self, window_height):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.setheading(270)
        self.speed("fastest")
        self.top_height = window_height/2
        self.bottom_height = -1 * self.top_height
        self.pensize(1)
        self.set_initial_position()
        self.draw_net()

    def draw_net(self):

        pen_down = True
        while self.ycor() > self.bottom_height:
            self.forward(20)
            if pen_down:
                self.penup()
            else:
                self.pendown()
            pen_down = not pen_down

    def set_initial_position(self):
        self.penup()
        self.setposition(0, self.top_height)
        self.pendown()