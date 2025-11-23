import higherlower_art
import random
import os

higherlower_art.logo()

def compare(followers1,followers2):
    if followers1 > followers2:
        return True
    return False

def clear():
    os.system('cls')

data=[
    {"name": "Instagram", "description": "Social media platform", "country": "United States", "followers": 500},
    {"name": "Cristiano Ronaldo", "description": "Footballer", "country": "Portugal", "followers": 600},
    {"name": "Lionel Messi", "description": "Footballer", "country": "Argentina", "followers": 480},
    {"name": "Selena Gomez", "description": "Musician and actress", "country": "United States", "followers": 430},
    {"name": "Kylie Jenner", "description": "Reality TV star", "country": "United States", "followers": 400},
    {"name": "Dwayne Johnson", "description": "Actor and wrestler", "country": "United States", "followers": 390},
    {"name": "Ariana Grande", "description": "Musician and actress", "country": "United States", "followers": 380},
    {"name": "Kim Kardashian", "description": "Reality TV star", "country": "United States", "followers": 360},
    {"name": "Beyoncé", "description": "Musician", "country": "United States", "followers": 320},
    {"name": "Taylor Swift", "description": "Musician", "country": "United States", "followers": 280},
    {"name": "Justin Bieber", "description": "Musician", "country": "Canada", "followers": 290},
    {"name": "Kendall Jenner", "description": "Model and reality TV star", "country": "United States", "followers": 270},
    {"name": "National Geographic", "description": "Magazine", "country": "United States", "followers": 260},
    {"name": "Jennifer Lopez", "description": "Musician and actress", "country": "United States", "followers": 250},
    {"name": "Neymar Jr", "description": "Footballer", "country": "Brazil", "followers": 220},
    {"name": "Nicki Minaj", "description": "Musician", "country": "Trinidad and Tobago", "followers": 210},
    {"name": "Miley Cyrus", "description": "Musician and actress", "country": "United States", "followers": 200},
    {"name": "Katy Perry", "description": "Musician", "country": "United States", "followers": 190},
    {"name": "Khloe Kardashian", "description": "Reality TV star", "country": "United States", "followers": 180},
    {"name": "Virat Kohli", "description": "Cricketer", "country": "India", "followers": 265}
]

score=0

while True:
    option1=random.choice(data)
    option2=random.choice(data)
    if option1==option2:
        continue

    print(f"Option A: {option1["name"]} is a {option1["description"]} in {option1["country"]}")
    higherlower_art.vs()
    print(f"Option B: {option2["name"]} is a {option2["description"]} in {option2["country"]}")
    option=input('Who has the most instagram followers?? Type "A" or Type "B"\n').lower()

    if option=="a":
        if compare(option1["followers"], option2["followers"]):
            score+=1
            clear()
            higherlower_art.logo()
            print(f"Correct! Your score is {score}\n")
        else:
            clear()
            higherlower_art.logo()
            print(f"Wrong! Your score is {score}")
            exit()
    elif option=="b":
        if compare(option2["followers"], option1["followers"]):
            score+=1
            clear()
            higherlower_art.logo()
            print(f"Correct! Your score is {score}\n")
        else:
            clear()
            higherlower_art.logo()
            print(f"Wrong! Your score is {score}")
            exit()
    else:
        print("Invalid Option")
        exit()