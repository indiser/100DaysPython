from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import json


print("-----------------------Extracted The Data----------------------------")
zillow_clone="https://appbrewery.github.io/Zillow-Clone/"

response=requests.get(url=zillow_clone)

soup=BeautifulSoup(response.text,"html.parser")

list_of_address=[]
list_of_prices=[]
list_of_links=[]
# Price
prices=soup.select(selector="span.PropertyCardWrapper__StyledPriceLine")

for price in prices:
    list_of_prices.append(price.getText().strip().replace("/mo","").replace("+","").replace("1 bd","").replace("1bd","").replace("$","").replace(",",""))

# Address
addresses=soup.find_all("address")

for address in addresses:
    list_of_address.append(address.getText().strip())

zillow_links=soup.find_all(name="a",class_="StyledPropertyCardDataArea-anchor")

for zillow_link in zillow_links:
    list_of_links.append(zillow_link.get("href").strip())

all_listings=[]

for price,address,link in zip(list_of_prices,list_of_address,list_of_links):
    if int(price) < 3000:
        listing_obj={
            'price':int(price),
            'address':address,
            'link':link
        }
        all_listings.append(listing_obj)

with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day53/temp.json",'w',encoding="utf-8") as filp:
    json.dump(all_listings,filp,indent=4)


print("-----------------------Putting it in Docs----------------------------")

google_docs="https://docs.google.com/forms/d/e/1FAIpQLSd5clZo0cHZMPy4_0Hz-PJJ6M06q1dLFOfYM900xXEwfQAzLw/viewform?usp=publish-editor"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(google_docs)

for i in range(len(all_listings)):
    try:
        first_question=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        second_question=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        third_question=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        submit_button=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        first_question.send_keys(all_listings[i]['address'])
        second_question.send_keys(all_listings[i]['price'])
        third_question.send_keys(all_listings[i]['link'])

        time.sleep(1)
        submit_button.click()
        
        submit_another_response=driver.find_element(By.LINK_TEXT,value="Submit another response")
        time.sleep(3)
        submit_another_response.click()
    except:
        print("Error Occurred")

print("-----------------------Done----------------------------")
driver.quit()