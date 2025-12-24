from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<strong> {function()} </strong>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em> {function()} </em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u> {function()} </u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
        "<p> This is a paragraph.</p>" \
        "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjNqeTIwZDg3aHJycmJldXl1dWpqcHZjb3V6bHliM2szY3ZsMWppMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohzdTQ62HVXIAlL7W/giphy.gif'>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "BYE!"



if __name__=='__main__':
    app.run(debug=True)