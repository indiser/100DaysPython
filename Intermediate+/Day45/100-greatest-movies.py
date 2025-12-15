from bs4 import BeautifulSoup
import requests
import random
import re
import os

pattern=re.compile(r'^\d+\s*—\s*\d+$')

url="https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
response=requests.get(url=url,headers=headers)

webpage_html=response.text
soup=BeautifulSoup(webpage_html,"html.parser")
movies=soup.select(selector="h2 strong")

movie_names=[movie.getText() for movie in movies]
reversed_movie_list=movie_names[::-1]

with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day45/movies.txt","w",encoding="utf-8") as filp:
    for name_of_the_movie in reversed_movie_list:
        if pattern.match(name_of_the_movie.strip()):
            continue
        filp.write(f"{name_of_the_movie}\n")



watched_movies = []

if os.path.exists("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day45/watched_movie.txt"):
    with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day45/watched_movie.txt", "r", encoding="utf-8") as filp:
        watched_movies = [line.strip() for line in filp.readlines()]


with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day45/movies.txt", "r", encoding="utf-8") as filp:
    contents = [line.strip() for line in filp.readlines()]


available_movies = [movie for movie in contents if movie not in watched_movies and movie != ""]


if len(available_movies) == 0:
    print("You have watched everything! Delete 'watched_movie.txt' to start over.")
else:
    random_movie = random.choice(available_movies)
    print(f"Watch: {random_movie}")

    # Append the choice to the watched file so we remember next time
    with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day45/watched_movie.txt", "a", encoding="utf-8") as filp:
        filp.write(f"{random_movie}\n")
    
    print(f"Movies remaining: {len(available_movies) - 1}")