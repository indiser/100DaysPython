print("Thank You For Choosing Python Pizza Deliveries")

print("----------------------------------------------------------------------------------------------\n")

Small=15
Medium=20
Large=25
pepperoni_for_small=2
pepperoni_for_medium_or_large=3
extra_cheese_on_pizza=1
print(f"Price of Small size Pizza:${Small}")
print(f"Price of Medium size Pizza:${Medium}")
print(f"Price of Large size Pizza:${Large}")
print(f"Price For Pepperoni on Small size Pizza:${pepperoni_for_small}")
print(f"Price For Pepperoni on Medium or Large size Pizza:${pepperoni_for_medium_or_large}")
print(f"Price For Extra Cheese on Pizza:${extra_cheese_on_pizza}")

print("----------------------------------------------------------------------------------------------\n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
total_price=0
print("----------------------------------------------------------------------------------------------\n")

if size=="S" or size=="s":
    total_price+=Small
    if add_pepperoni=="Y" or add_pepperoni=="y":
        total_price+=pepperoni_for_small
    else:
        if extra_cheese=="Y" or extra_cheese=="y":
            total_price+=extra_cheese_on_pizza
elif size=="M" or size=="m":
    total_price+=Medium
    if add_pepperoni=="Y" or add_pepperoni=="y":
        total_price+=pepperoni_for_medium_or_large
    else:
        if extra_cheese=="Y" or extra_cheese=="y":
            total_price+=extra_cheese_on_pizza
elif size=="L" or size=="l":
    total_price+=Large
    if add_pepperoni=="Y" or add_pepperoni=="y":
        total_price+=pepperoni_for_medium_or_large
    else:
        if extra_cheese=="Y" or extra_cheese=="y":
            total_price+=extra_cheese_on_pizza
else:
    print("Invalid Input")
    exit()

    
print(f"Your Total Order Price is: ${total_price}")