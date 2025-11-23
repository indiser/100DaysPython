import calc_art

calc_art.logo()

def sum(a, b):
    return a+b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
def subtract(a, b):
    return a-b
def remainder(a, b):
    return a%b

operations={
    "+":sum,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "%":remainder
}

result=None
while True:
    if result is None:
        firstNum=float(input("Enter the first number:\n"))
    else:
        firstNum=result
        
    print('Operations:\n')
    for key in operations:
        print(key)
    user_choice=input("Enter the choice of operation:\n")
    secondNum=float(input("Enter the second number:\n"))
    
    if user_choice in operations:
        function=operations[user_choice]
        answer=function(firstNum, secondNum)
        print(f"{firstNum} {user_choice} {secondNum} = {answer}\n")
        result=answer
    else:
        print("Invalid operation")
        continue

    proceed=input('Type "Yes" to continue or Type "No" to exit..\n').lower()
    print(f"What do you want to do with the pervious result {result}??")
    if proceed!="yes":
        break