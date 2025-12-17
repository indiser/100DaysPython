import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options
import time

# \@echo off
# echo Launching Chrome in Debug Mode...
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\ranab\OneDrive\Desktop\100Days Python\Intermediate+\Day51\chrome_profile"
# First rn the command in cmd. then open the x website login manually then run script.



# ---------------- Speed Test Section ----------------
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

# SuccessFul Speed Test
speedTest_url="https://speedtest.net/"
driver.get(speedTest_url)

try:
    print("Pressing The Trust Button")
    time.sleep(5)
    agreement=driver.find_element(By.XPATH,value='//*[@id="onetrust-accept-btn-handler"]')
    agreement.click()
except:
    print("Something Went Wrong")

try:
    print("Pressing The Go Button...")
    time.sleep(5)
    speed_test_button=driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]')
    speed_test_button.click()
    time.sleep(45)

    result_id=driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')

    download_speed=driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

    upload_speed=driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

    print("SpeeD Test Complete")
except:
    print("Something Went Wrong")


formatted_msg=f"Hey Internet Provider, Why is my internet speed {download_speed.text}down/{upload_speed.text}up when i pay for 60down/10ups??"

print(formatted_msg)

driver.quit()

# ---------------- Twitter Bot Section ----------------
# 1. Connect to the existing Chrome window
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# We use standard webdriver because the browser is ALREADY open
driver = webdriver.Chrome(options=chrome_options)

print("Connected to Chrome!")
print("Current URL:", driver.current_url)

# 2. Verify we are on Twitter
if "x.com" in driver.current_url or "twitter.com" in driver.current_url:
    print("Found Twitter. Attempting to post...")
    
    try:
        # 3. Simple Post Logic
        # Click the composer
        composer = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
        composer.click()
        
        # Type message
        composer.send_keys(formatted_msg)
        
        # Click Post (Uncomment to actually post)
        time.sleep(5)
        post_btn = driver.find_element(By.XPATH, "//button[@data-testid='tweetButtonInline']")
        post_btn.click()
        
        print("Script finished successfully.")
        
    except Exception as e:
        print(f"Could not find elements. Error: {e}")
else:
    print("You are not on Twitter! Please navigate to Twitter in the browser window manually.")

# Do NOT quit the driver, or it will close your manual window.