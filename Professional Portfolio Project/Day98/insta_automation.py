import time
import os
import json
import glob
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

script_path = os.path.dirname(os.path.abspath(__file__))
scripts_path = os.path.join(script_path, "scripts.json")
trend = os.path.join(script_path,"TrendingDescription.txt")

with open(trend,"r",encoding="utf-8") as filp:
    contents=filp.read()

def get_stealth_browser():
    """Initializes a stealth browser using Chrome profile."""
    options = uc.ChromeOptions()
    # profile_path = r"C:\Users\ranab\AppData\Local\Google\Chrome\User Data\BotProfile"
    profile_path = os.path.join(os.getcwd(), "IgBotProfile")
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--log-level=3")
    options.add_argument("--window-size=1280,800")
    
    print("Launching stealth browser...")
    driver = uc.Chrome(options=options, version_main=145)
    time.sleep(2)
    return driver

def get_video_metadata(video_id):
    """Get metadata from scripts.json for a video ID."""
    with open(scripts_path, "r", encoding="utf-8") as f:
        scripts = json.load(f)
    
    for script in scripts:
        if script.get("posted_instagram") == True:
            continue
        if script["id"] == video_id:
            return script
    return None

def mark_as_posted(video_id):
    """Marks video as posted to Instagram in scripts.json."""
    with open(scripts_path, "r", encoding="utf-8") as f:
        scripts = json.load(f)
    
    for script in scripts:
        if script["id"] == video_id:
            script["posted_instagram"] = True
            break
    
    with open(scripts_path, "w", encoding="utf-8") as f:
        json.dump(scripts, f, indent=4, ensure_ascii=False)

def upload_reel(driver, video_path: str):
    """Upload a reel to Instagram via Selenium."""
    try:
        print(f"Current URL: {driver.current_url}")
        print("Looking for Create button...")

        wait=WebDriverWait(driver,10)
        
        # Click Create button
        create_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Create')]/ancestor::a | //svg[@aria-label='New post']/ancestor::a | //a[@href='#']//*[name()='svg'][@aria-label='Create']/ancestor::a"))
        )
        print("Create button found, clicking...")
        create_btn.click()
        time.sleep(2)
        
        # Click Post button to open file dialog
        post_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Post')]"))
        )
        print("Clicking The Post Button..")
        post_button.click()
        time.sleep(2)

        print("Hunting for the hidden file input tag...")
        file_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        print(f"Uploading: {os.path.abspath(video_path)}")
        file_input.send_keys(os.path.abspath(video_path))
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
        time.sleep(10)

        share_btn=wait.until(
            EC.element_to_be_clickable((By.XPATH,"//div[@role='button' and text()='Share']"))
        )
        share_btn.click()
        print("Shared")
        time.sleep(300)
        
        print("Refreshing page for next upload...")
        driver.refresh()
        time.sleep(10)

        return True
    except Exception as e:
        print(f"❌ Upload error: {e}")
        return False

if __name__ == "__main__":
    video_files = glob.glob("ready_to_upload/*.mp4")
    
    if not video_files:
        print("No videos found in ready_to_upload/ folder")
    else:
        print(f"Found {len(video_files)} videos to upload\n")
        
        driver = get_stealth_browser()
        
        try:
            print("Navigating to Instagram...")
            driver.get("https://www.instagram.com/")
            time.sleep(8)
            print(f"Current URL: {driver.current_url}")
            print(f"Page title: {driver.title}")
            
            # Check if logged in
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Create')] | //svg[@aria-label='New post'] | //a[@href='#']//*[name()='svg'][@aria-label='Create']"))
                )
                print("✅ Logged in successfully")
            except:
                print("❌ Not logged in or page didn't load properly")
                print("Please manually log in...")
                input("Press Enter after logging in...")
            
            success_count = 0
            for video_path in video_files:
                filename = os.path.basename(video_path)
                video_id = filename.replace(".mp4", "").split("_")[-1]
                metadata = get_video_metadata(video_id)
                
                if metadata:
                    print(f"Uploading: {filename}")
                    if upload_reel(driver, video_path):
                        mark_as_posted(video_id)
                        success_count += 1
                        print(f"✅ Uploaded: {video_id}\n")
                    else:
                        print(f"❌ Failed: {video_id}\n")
                else:
                    print(f"⚠️ No metadata found for {video_id}, skipping\n")
            
            print(f"\n{'='*50}")
            print(f"Upload complete: {success_count}/{len(video_files)} successful")
        
        finally:
            print("Closing browser...")
            driver.quit()
