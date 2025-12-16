import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
load_dotenv()

email=os.environ.get("LINKDIN_EMAIL")
password=os.environ.get("LINKDIN_PASSWORD")

linkdin_url="https://www.linkedin.com/jobs/search/?currentJobId=4335474584&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(linkdin_url)

try:
    wait = WebDriverWait(driver, 5)
    reject_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[action-type="DENY"]')))
    reject_button.click()
    time.sleep(2)
except:
    print("Cookie rejection button not found, continuing...")
    time.sleep(2)

try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".overflow-hidden")))
except:
    print("Modal still visible, proceeding anyway...")


time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
driver.execute_script("arguments[0].click();", sign_in_button)


username=driver.find_element(By.ID,value="username")
username.send_keys(email)

passkey=driver.find_element(By.ID, value="password")
passkey.send_keys(password)

submit_button=driver.find_element(By.CSS_SELECTOR,value=".login__form_action_container button")
submit_button.send_keys(Keys.ENTER)

# time.sleep(30)
# otp_submission=driver.find_element(By.CSS_SELECTOR,value=".form__action button")
# otp_submission.click()

try:
    print("Saving The Job....")
    time.sleep(20)
    save_job=driver.find_element(By.XPATH,value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[6]/div/button')
    save_job.click()
except:
    print("Error Occurred")

try:
    print("Following The Company....")
    driver.get("https://www.linkedin.com/company/playtech/")
    time.sleep(20)
    follow_button=driver.find_element(By.CLASS_NAME, value="follow")
    follow_button.click()
except:
    print("Error Occurred")

try:
    time.sleep(5)
    cancel_button=driver.find_element(By.CSS_SELECTOR,value="span button")
    cancel_button.click()
except:
    print("Error Occurred")

driver.quit()