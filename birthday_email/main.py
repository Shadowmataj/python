##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "christianmataj1@gmail.com"
APP_PASSWORD = "ytrdilgxckajmouv"
today_birthdays = []

def send_email(**kwargs):
    letter_to_send = kwargs["letter"]
    name = kwargs["name"]
    email = kwargs["email"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject: Happy Birthday {name}!\n\n{letter_to_send}")
# 1. Update the birthdays.csv
    #DONE
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
months_birthdays = data[data.month == today.month]
if len(months_birthdays) > 0:
    today_birthdays = months_birthdays[data.day == today.day]
    today_birthdays_list = today_birthdays.to_dict(orient="records")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(today_birthdays) > 0:
    for birthday_person in today_birthdays_list:
        random_letter = random.randint(1,3)
        with open(f"letter_templates/letter_{random_letter}.txt") as letter:
            chosen_letter = letter.read()
            finished_letter = chosen_letter.replace("[NAME]", birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        send_email(letter=finished_letter, name=birthday_person["name"], email=birthday_person["email"])
else:
    print("Sorry, there's no birthday today")

