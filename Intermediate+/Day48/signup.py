from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

appbrewry_url="https://secure-retreat-92358.herokuapp.com/"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(appbrewry_url)

first_name=driver.find_element(By.NAME,value="fName")
first_name.send_keys("xoxo")

last_name=driver.find_element(By.NAME,value="lName")
last_name.send_keys("yoyo")

email_name=driver.find_element(By.NAME,value="email")
email_name.send_keys("xoxoyoyo@gmail.com")

submit_button=driver.find_element(By.TAG_NAME, value="button")
submit_button.click()

driver.quit()