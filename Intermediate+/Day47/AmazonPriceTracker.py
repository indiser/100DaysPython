from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

gmail=os.environ.get("SENDER_GMAIL_ID")
gmail_pass=os.environ.get("EMAIL_APP_PASS")
reciver_gmail=os.environ.get("RECIVER_ADDRESS_EMAIL")

amazon_url="https://www.amazon.in/Passport-Portable-External-Drive-Black/dp/B07VTFN6HM/ref=sr_1_1_sspa?crid=KVRNN2O09DJU&dib=eyJ2IjoiMSJ9.wYy_lbuBFC5zadlsiraCS1Vd7eqvzR7txziz2bqKnPe2VaUrkAxFw3KxEPnjAdxKXqd8AKXLfevTbanbUvl86HQs9hp5BQOMlwlVwftplQXwHFLQ9p-Y0Cbh-NjGrwyrXVZZYsdEK3dgwpwCVGrORXgzcdDrVcR0Eqdr_RE3_c3MaIUMMLsluO9Nbiy4RbwDdhq_QjOl200j40qeTvES7cW-PCML1MUrll1B_DtvTx8.9kfI1w0Qq0UNBUY-0Uzp2swNTm4STy4oro2Yb7udbsk&dib_tag=se&keywords=2tb%2Bexternal%2Bhard%2Bdisk&qid=1765792310&sprefix=2tb%2Caps%2C276&sr=8-1-spons&aref=2PVcOCr4j6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

response=requests.get(url=amazon_url)
amazon_html=response.text

soup=BeautifulSoup(amazon_html,"html.parser")


product_name=soup.title.string

current_price=int(soup.find(class_="a-price-whole").getText().strip().replace(".","").replace(",",""))

target=3000

if current_price <= target:
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as connections:
            formatted_msg=f"Subject:Low Price On Hard Drive\n\n {product_name} is in all time low price of only {current_price} INR.\nHere is the url:{amazon_url}"
            connections.starttls()
            connections.login(user=gmail,password=gmail_pass)
            connections.sendmail(
                from_addr=gmail,
                to_addrs=reciver_gmail,
                msg=formatted_msg
            )
        print("Messege Sent")
    except:
        print("Messege Not Sent")
else:
    print(f"Current Price is {current_price} INR. above target price of {target} INR.")