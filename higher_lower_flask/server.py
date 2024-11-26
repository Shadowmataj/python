import random

from flask import Flask

number: int

app = Flask(__name__)

@app.route("/")
def guess_a_number():
    global number
    number = random.randint(0, 9)
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>')

@app.route("/<int:guess_number>")
def guess(guess_number):
    global number
    print(number)
    if guess_number < number:
        return ('<h1 style = "color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>')
    elif guess_number > number:
        return ('<h1 style = "color: purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img>')

    return ('<h1 style="color: green">You found me!</h1>'
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>')


if __name__ == "__main__":
    app.run(debug=True)