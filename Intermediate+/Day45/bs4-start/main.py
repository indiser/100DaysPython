from bs4 import BeautifulSoup
with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day45/bs4-start/website.html", encoding='utf-8') as filp:
    contents=filp.read()
soup=BeautifulSoup(contents,"html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.p)

all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)

for tags in all_anchor_tags:
    # print(tags.getText())
    print(tags.get("href"))

heading=soup.find(name="h1",id="name")
print(heading.string)

section_heading=soup.find(name="h3",class_="heading")
print(section_heading.get("class"))

company_url=soup.select_one(selector="p a")
print(company_url)

headings=soup.select(selector=".heading")
print(headings)