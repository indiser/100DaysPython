import math
def paint_calc(height,width,coverage):
    number_of_cans=(height*width)/coverage
    print(f"The number of cans are:{math.ceil(number_of_cans)}")

height=int(input("Enter the height:\n"))
width=int(input("Enter the width:\n"))
coverage=int(input("Enter the coverage area:\n"))

paint_calc(height=height,width=width,coverage=coverage)