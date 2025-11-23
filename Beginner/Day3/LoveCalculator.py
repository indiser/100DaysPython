print("The Love Calculator is calculating your score.....")
name1 = input("What is your name??\n")
name2 = input("What is your Partnes's name??\n")

combined_name=name1+name2
lower_cased=combined_name.lower()

T=lower_cased.count("t")
R=lower_cased.count("r")
U=lower_cased.count("u")
E=lower_cased.count("e")

first_digit=T+R+U+E

L=lower_cased.count("l")
O=lower_cased.count("o")
V=lower_cased.count("v")
E=lower_cased.count("e")


second_digit=L+O+V+E

combined=str(first_digit)+str(second_digit)
loveScore=int(combined)

if loveScore <= 10 or loveScore >=90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <=50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")