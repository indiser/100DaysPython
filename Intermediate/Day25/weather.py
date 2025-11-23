import pandas as pd
import numpy as np
import csv

with open("weather-data.csv") as filp:
    data=csv.reader(filp)
    temperatures=[]
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    # print(temperatures)


data=pd.read_csv("weather-data.csv")
# print(data["temp"])


temp_list=data["temp"].to_list()
# sum=0
# for temperature in temp_list:
#     sum+=temperature

# avg=sum/len(temp_list)
# print(avg)
# print(data.max())
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

monday=data[data["day"]=="Monday"]
c=monday["temp"][0]
f=(c*1.8)+32
print(f)
