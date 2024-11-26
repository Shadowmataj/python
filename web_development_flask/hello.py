from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasise(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"

@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)

# from time import sleep
#
#
# def decorator_function(function):
#     def wrapper_function():
#         sleep(2)
#         #do something before
#         function()
#         #do something after
#     return wrapper_function()
#
# @decorator_function
# def say_hello():
#     print("hello")
#
# @decorator_function
# def say_bye():
#     print("good bye!")
#
# @decorator_function
# def say_greeting():
#     print("How are you?")

