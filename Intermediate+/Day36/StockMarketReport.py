import requests
import os
import smtplib
from dotenv import load_dotenv
import json


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


load_dotenv()
email = os.environ.get("EMAIL")
email_app_pass = os.environ.get("EMAIL_APP_PASS")
address_email = os.environ.get("ADDRESS_EMAIL")
alphavantage_api_key=os.environ.get("ALPHAVANTAGE_API")
news_api_key=os.environ.get("NEWS_API")


# Percentage Calculation
def percentage_difference(old_price,new_price):
    if old_price==0:
        raise ValueError("Old price cannot be zero")
    return ((old_price-new_price)/old_price)*100



# News API
news_parameters={
    "q":COMPANY_NAME,
    "apiKey":news_api_key
} 
news_url="https://newsapi.org/v2/everything"
news_reponse=requests.get(url=news_url,params=news_parameters)
news_reponse.raise_for_status()

news_data=news_reponse.json()["articles"][0]
news_title=news_data["title"]
news_description=news_data["description"]


# Stock API
parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":alphavantage_api_key
}
stock_url="https://www.alphavantage.co/query"
stock_response=requests.get(url=stock_url,params=parameters)
stock_response.raise_for_status()

time_series=stock_response.json()["Time Series (Daily)"]
dates=list(time_series.keys())

most_recent_date=dates[0]
previous_date=dates[1]

yesterdays_data=time_series[most_recent_date]
day_before_yesterdays_data=time_series[previous_date]

old_closeing_price=day_before_yesterdays_data["4. close"]
new_closing_price=yesterdays_data["4. close"]

difference_in_percentage=percentage_difference(float(old_closeing_price),float(new_closing_price))


# Email Sending
if difference_in_percentage>=5 or difference_in_percentage <= -5:
    arrow = "🔺" if difference_in_percentage > 0 else "🔻"
    formatted_msg = f"Subject:{STOCK}: {arrow}{abs(difference_in_percentage):.2f}%\n\nHeadline: {news_title}\nBrief: {news_description}"
    
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=email, password=email_app_pass)
            connection.sendmail(
                from_addr=email,
                to_addrs=address_email,
                msg=formatted_msg.encode('utf-8')
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
else:
    print(f"No significant change in stock price: {difference_in_percentage:.2f}%")