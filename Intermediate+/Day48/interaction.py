from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

wikipedia_url="https://en.wikipedia.org/wiki/Main_Page"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(wikipedia_url)

# articles_number=driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(f"Articles: {articles_number.text}")
# articles_number.click()

# all_portals=driver.find_element(By.LINK_TEXT,value="Content portals")
# all_portals.click()


# Wait for search element to be clickable, then interact
wait = WebDriverWait(driver, 10)
search = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
search.click()
search.send_keys("Python", Keys.ENTER)
# driver.quit()