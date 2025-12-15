# from bs4 import BeautifulSoup
# import requests

# url="https://news.ycombinator.com/"

# response=requests.get(url=url)

# yc_web_page=response.text

# soup=BeautifulSoup(yc_web_page,"html.parser")
# anchor_tags=soup.select(selector="span", class_="titleline")
# for tags in anchor_tags:
#     print(tags.getText())
#     print(tags.get("href"))

from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the page title
title = soup.find("title").getText()
print(f"Title: {title}\n")

# Get all links (headlines and URLs)
stories = soup.select("span.titleline > a")

for story in stories:
    headline = story.getText()
    link = story.get("href")
    # Find the upvote count (score is in the next row)
    score_tag = story.find_parent("tr").find_next_sibling("tr").find("span", class_="score")
    upvotes = score_tag.getText().split()[0] if score_tag else "N/A"
    print(f"Headline: {headline}")
    print(f"Link: {link}")
    print(f"Upvotes: {upvotes}")
    print()
# print(f"Headline: {headline}")
# print(f"Link: {link}")
upvote=soup.select_one(selector=".score")
print(upvote)
