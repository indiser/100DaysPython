import pandas as pd

data=pd.read_csv("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate/Day26/nato_phonetic_alphabet.csv")

new_dict={row["letter"]:row["code"] for (index,row) in data.iterrows()}



def generate():
    user_input=input("Enter a word: ").upper()
    
    try:
        list1=[new_dict[i] for i in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet allowed")
        generate()
    else:
        print(list1)

generate()