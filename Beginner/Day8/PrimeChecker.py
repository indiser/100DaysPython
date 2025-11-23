
def primeChecker(number):
    is_Prime=True
    for i in range(2,number):
        if number % i==0:
            is_Prime=False
    if is_Prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


num=int(input("Enter the number:\n"))
primeChecker(num)