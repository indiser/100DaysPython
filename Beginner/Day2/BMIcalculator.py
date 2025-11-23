weight=float(input("Enter the weight(kg.)\n"))
height=float(input("Enter the height(m)\n"))

bmi=weight/(height**2)
print(f"The BMI of the person with weight {weight} and {height} is: {bmi}")