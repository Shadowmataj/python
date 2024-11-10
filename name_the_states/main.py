import turtle
import pandas


screen = turtle.Screen()
screen.title("Name The State")
image =  "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

named_states = []
missed_states = []
data = pandas.read_csv("50_states.csv")
total_states = len(data)
all_states = data.state.to_list()

while len(named_states) < total_states:

    answer_state = screen.textinput(title=f"{len(named_states)}/{total_states} States Correct", prompt="What's another state?").title()

    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in named_states]
        states_to_learn = pandas.DataFrame(missed_states, columns=["state"])
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in named_states:
        state_data = data[data.state == answer_state]
        pen.goto(state_data.x.item(), state_data.y.item())
        pen.write(arg=f"{answer_state}")
        named_states.append(answer_state)


screen.exitonclick()