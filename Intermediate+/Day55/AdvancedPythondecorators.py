class User:
    def __init__(self,name):
        self.name=name
        self.is_logged_in=False

def is_aunthenticated(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in==True:
            function(args[0])
    return wrapper

@is_aunthenticated
def create_blog_post(user):
    print(f"This is {user.name} blog post")

new_user=User("God")
new_user.is_logged_in=True
create_blog_post(new_user)