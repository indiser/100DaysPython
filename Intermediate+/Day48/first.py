from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

amazon_url="https://www.amazon.in/Passport-Portable-External-Drive-Black/dp/B07VTFN6HM/ref=sr_1_1_sspa?crid=KVRNN2O09DJU&dib=eyJ2IjoiMSJ9.wYy_lbuBFC5zadlsiraCS1Vd7eqvzR7txziz2bqKnPe2VaUrkAxFw3KxEPnjAdxKXqd8AKXLfevTbanbUvl86HQs9hp5BQOMlwlVwftplQXwHFLQ9p-Y0Cbh-NjGrwyrXVZZYsdEK3dgwpwCVGrORXgzcdDrVcR0Eqdr_RE3_c3MaIUMMLsluO9Nbiy4RbwDdhq_QjOl200j40qeTvES7cW-PCML1MUrll1B_DtvTx8.9kfI1w0Qq0UNBUY-0Uzp2swNTm4STy4oro2Yb7udbsk&dib_tag=se&keywords=2tb%2Bexternal%2Bhard%2Bdisk&qid=1765792310&sprefix=2tb%2Caps%2C276&sr=8-1-spons&aref=2PVcOCr4j6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

# keep it open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# Wait for the price element to load (max 10 seconds)
# wait = WebDriverWait(driver, 10)
# current_price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
# print(f"Current Price is:{current_price.text} INR.")

search_bar=driver.find_element(By.NAME,value="q")
print(search_bar.get_attribute("placeholder"))

submit_button=driver.find_element(By.ID,value="submit")
print(submit_button.size)

docs_link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(docs_link.text)

bug=driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug.text)
# driver.close()
driver.quit()