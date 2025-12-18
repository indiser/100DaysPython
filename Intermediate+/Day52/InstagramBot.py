import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()

# --- CONFIGURATION ---
INSTA_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTA_PASS = os.environ.get("INSTAGRAM_PASSWORD")
TARGET_ACCOUNT = "chefsteps" 
# ---------------------

# 1. SETUP DRIVER
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

try:
    # 2. LOGIN
    print("--- Logging In ---")
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    try:
        username = driver.find_element(By.NAME, "username")
        username.send_keys(INSTA_USERNAME)
        password = driver.find_element(By.NAME, "password")
        password.send_keys(INSTA_PASS, Keys.ENTER)
    except:
        print("Standard login failed. Check internet or selectors.")
        email=driver.find_element(By.NAME,value="email")
        email.send_keys(INSTA_USERNAME)

        passWord=driver.find_element(By.NAME,value="pass")
        passWord.send_keys(INSTA_PASS,Keys.ENTER)

    # Wait for login to complete (Adjust if your internet is slow)
    time.sleep(10)

    # 3. NAVIGATE TO PROFILE
    print(f"--- Navigating to {TARGET_ACCOUNT} ---")
    driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
    time.sleep(5)

    # 4. OPEN FOLLOWERS LIST
    print("--- Opening Followers List ---")
    followers_link = driver.find_element(By.XPATH, f"//a[contains(@href, '/{TARGET_ACCOUNT}/followers/')]")
    followers_link.click()
    time.sleep(5)

    # 5. FIND THE MODAL (Fixed using your file analysis)
    print("--- Locating Modal ---")
    try:
        # We target the specific style attribute found in your edit.txt
        # This div has "overflow: hidden auto" which creates the scrollbar.
        modal = driver.find_element(By.XPATH, "//div[contains(@style, 'overflow: hidden auto')]")
        print("Success: Modal found via Style attribute.")
    except:
        print("CRITICAL ERROR: Could not find modal. Script cannot scroll.")
        exit()

    # 6. SCROLL AND FOLLOW LOOP
    print("--- Starting Scroll Loop ---")
    
    for i in range(5):
        print(f"Batch {i+1}...")
        
        # A. Click visible buttons
        # We look for buttons containing the text "Follow" to avoid unfollowing people
        follow_buttons = driver.find_elements(By.XPATH, "//button[div/div[text()='Follow']]")
        
        for btn in follow_buttons:
            try:
                # JavaScript click is required to click 'through' any invisible overlays
                driver.execute_script("arguments[0].click();", btn)
                print(" -> Followed user")
                time.sleep(2) # Sleep is mandatory to avoid soft-bans
            except Exception as e:
                print(" -> Skipped button (Already followed or error)")
        
        # B. Scroll the modal
        try:
            # Teleport the scrollbar to the bottom of the found modal
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3) # Wait for new users to load
        except Exception as e:
            print(f"Scroll failed: {e}")
            break

except Exception as e:
    print(f"An error occurred: {e}")

print("Done.")
# driver.quit()