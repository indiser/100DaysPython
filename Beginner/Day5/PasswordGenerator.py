import random

print(r'''
   |\                     /)
 /\_\\__               (_//
|   `>\-`     _._       //`)
 \ /` \\  _.-`:::`-._  //
  `    \|`    :::    `|/
        |     :::     |
        |.....:::.....|
        |:::::::::::::|
        |     :::     |
        \     :::     /
         \    :::    /
          `-. ::: .-'
           //`:::`\\
          //   '   \\
         |/         \\
''')

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassWord Generator.")
letter_input=int(input("How many letters do you want in your password??\n"))
symbol_input=int(input("How many symbols would you like??\n"))
number_input=int(input("How many many numbers would you like??\n"))

passWord=""

for i in range(0,letter_input-1):
    rand_letter=random.choice(letters)
    passWord+=rand_letter

for j in range(0,symbol_input-1):
    rand_symbol=random.choice(symbols)
    passWord+=rand_symbol

for k in range(0,number_input):
    rand_number=random.choice(numbers)
    passWord+=rand_number

print(f"Level 1 Password:{passWord}")

random_passWord=''.join(random.sample(passWord,len(passWord)))
print(f"Level Max Password:{random_passWord}")