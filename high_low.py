import random
from flask import Flask
app = Flask(__name__)

def make_h1(message):
    def wrapped():
        return "<h1>" + message() + "</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    return wrapped

def get_effects(func):
    def wrapped1(dig):
        text = func(dig)


    return wrapped1

@app.route('/')
@make_h1
def hello_world():
    global number
    number = random.randint(0, 9)
    print(number)
    return 'Guess a number between 0 and 9'





@app.route('/<int:dig>')
def number_check(dig):
    if dig < number:
        return " <h1 style='color:red;'>  Too LoWWWW </h1>" \
               "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif dig > number:
        return "<h1 style='color:blue;'> TOO HIGHTTTTTTT</h1>" \
               "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color:green;'> You GOT ITTTTTTT </h1>" \
               "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"





if __name__ == "__main__":
    app.run(debug=True)
