import smtplib
from bs4 import BeautifulSoup
import requests
import os

URL = "AMAZON_URL"
POINT_PRICE = 3000

email = os.environ.get("EMAIL")
google_key = os.environ.get("GOOGLE_KEY")

def send_email(price:float, title:str):
    if price <= POINT_PRICE:
        message = f"Subject: The time to buy is now!\n\nThe {title} is now ${price}\nlink: {URL}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=google_key)
            mail_response = connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=message,
            )
    else:
        print("No yet")

def scraping_code():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
    }

    url_response = requests.get(url=URL, headers=headers)
    url_soup = BeautifulSoup(url_response.text, "html.parser")


    price_element = url_soup.find(class_="aok-offscreen")
    price_text = price_element.getText().split()[0].strip().replace(",","_")
    price = round(float(price_text[1:]), 2)

    title_element = url_soup.find(id="productTitle")
    title_text = title_element.getText().replace("\r\n", "").split()
    title = str(" ".join(title_text).encode('utf-8').strip())

    send_email(price,title)

scraping_code()

