
def loggin_decorator(function):
    def wrapper(*args):
        print(f"you called a function {function.__name__}{args}")
        print(f"It retured:{function(args[0],args[1],args[2])}")
    return wrapper



@loggin_decorator
def a_function(a,b,c):
    return a*b*c

a_function(1,2,3)