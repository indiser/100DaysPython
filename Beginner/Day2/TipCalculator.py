print("Welcome to a simple tip calculator")

total=float(input("What is the total amount??\n$"))

tip=int(input("What percentage of tip do you want to put in?? 10, 12 or 20\n"))

splitBill=int(input("How many people do you want the tip to split in??\n"))

afterSplit=total+(total * (tip/100))
afterSplit=float(afterSplit/splitBill)
afterSplit=round(afterSplit,2)

print(f"Each person should pay ${afterSplit}")