weight=float(input("Enter the weight(kg.)\n"))
height=float(input("Enter the height(m)\n"))

bmi=float(weight/(height**2))

if bmi < 18.5:
    print("Underweight")
elif bmi <25:
    print("Normal weight")
elif bmi < 30:
    print("Slightly Overweight")
elif bmi < 35:
    print("Obesse")
else:
    print("Clinically Obesse")