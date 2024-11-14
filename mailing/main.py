#SIMPLE MAIL TRANSFER PROTOCOL
import smtplib
import datetime as dt
import random

APP_PASSWORD = "ytrdilgxckajmouv"

my_email = "email"
test_email = "email"

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=test_email,
            msg=f"Subject: The motivational quote of the day\n\n{quote}")


with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()

today = dt.datetime.now()
weekday = today.weekday()
if weekday == 2:
    quote_of_the_day = random.choice(quotes)
    send_email(quote_of_the_day)
