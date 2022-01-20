from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapped():
        b = f"<b>{function()}</b>"
        return b
    return wrapped

def make_em(function):
    def wrapped():
        b = f"<em>{function()}</em>"
        return b
    return wrapped

def make_u(function):
    def wrapped():
        b = f"<u>{function()}</u>"
        return b
    return wrapped

@app.route('/')
@make_bold
@make_em
@make_u
def hello_world():
    return 'Hello, World!'

@app.route('/<name>')
def hello_name(name):
    return f'<h1 style = "text-align: center">Hello, {name}!</h1><p> this is  a paragraph</p>' \
           f'<img src ="https://media.giphy.com/media/CJxXHfRAYvtqU/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
