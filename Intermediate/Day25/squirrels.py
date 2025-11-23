import pandas as pd


data=pd.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrles_count=len(data[data["Primary Fur Color"]=="Gray"])
print(grey_squirrles_count)
red_squirrles_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(red_squirrles_count)
black_squirrles_count=len(data[data["Primary Fur Color"]=="Black"])
print(black_squirrles_count)


squirrle={"Fur Color":["Gray","Red","Black"],"Count":[grey_squirrles_count,red_squirrles_count,black_squirrles_count]}

df=pd.DataFrame(squirrle)
df.to_csv("squirrle_count.csv")