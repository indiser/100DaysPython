from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.python.org")

times=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
events=[]
for items in times:
    events.append(items.text)
# print(events)

event_names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget .menu a")
event_list=[]
for names in event_names:
    event_list.append(names.text)
# print(event_list)

event_dict={}
for i in range(len(event_list)):
    event_dict[i]={

        "time":events[i],
        "name":event_list[i]
    }
print(event_dict)

driver.quit()