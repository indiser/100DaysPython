# def add(*args):
#     for i in args:
#         if type(i) == str:
#             return None
#         else:
#             sum=0
#             for i in args:
#                 sum+=i
#             return sum


# numbers=[]
# while True:
#     user_input=int(input("Enter The number and press 0 to stop:\n"))
#     if user_input==0:
#         break
#     numbers.append(user_input)

# print(add(*numbers))


def calculate(n,**kwargs):
    for key in kwargs:
        n+=kwargs[key]
    print(n)


calculate(4,one=1,two=2,three=3)