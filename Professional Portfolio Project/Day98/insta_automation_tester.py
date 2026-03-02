import time
import os
import json
import glob
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

with open("TrendingDescription.txt","r",encoding="utf-8") as filp:
    contents=filp.read()

options = uc.ChromeOptions()
profile_path = os.path.join(os.getcwd(), "IgBotProfile")
options.add_argument(f"--user-data-dir={profile_path}")
options.add_argument("--log-level=3")
options.add_argument("--window-size=1280,800")
    
driver = uc.Chrome(options=options, version_main=145)

driver.get("https://www.instagram.com/")

wait=WebDriverWait(driver,10)

create_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Create')]/ancestor::a | //svg[@aria-label='New post']/ancestor::a | //a[@href='#']//*[name()='svg'][@aria-label='Create']/ancestor::a"))
)
print("Create button found, clicking...")
create_btn.click()
time.sleep(3)

post_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Post')]"))
)
print("Clicking The Post Button..")
post_button.click()

print("Hunting for the hidden file input tag...")
file_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
)

video_to_upload=r"C:\Users\ranab\OneDrive\Desktop\AutoContent\ready_to_upload\Dirty_massages_1rguma6.mp4"

print(f"Injecting payload directly into the DOM: {video_to_upload}")
file_input.send_keys(video_to_upload)

time.sleep(5)

nxt_btn=wait.until(
    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Next')]"))
)
driver.execute_script("arguments[0].click();", nxt_btn)
print("Clicked the first next")
time.sleep(10)

nxt_btn_2=wait.until(
    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Next')]"))
)
driver.execute_script("arguments[0].click();", nxt_btn_2)
print("Clicked the second next")
time.sleep(10)

caption_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Write a caption...']"))
)
caption_box.click()
print("Clicked the caption")
time.sleep(10)

print("Loading payload into OS clipboard...")
pyperclip.copy(contents)

print("Executing native OS paste (CTRL+V)...")
# Natively fire CTRL+V directly into the active browser window
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
print("sent the caption")
time.sleep(30)

share_btn=wait.until(
    EC.element_to_be_clickable((By.XPATH,"//div[@role='button' and text()='Share']"))
)
share_btn.click()
print("Shared")
time.sleep(60)
