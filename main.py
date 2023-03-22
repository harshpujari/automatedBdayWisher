from datetime import datetime
import pandas
import random
import smtplib
import schedule
import time

MY_EMAIL = "harshpujari@outlook.com"
MY_PASSWORD = "abe_sale_password_dhoond_raha_hai_kya?"

def bDayWisher():
    today = datetime.now()
    today_tuple = (today.month, today.day)

    data = pandas.read_csv("birthdays.csv")
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
    if today_tuple in birthdays_dict:
        birthday_person = birthdays_dict[today_tuple]
        file_path = f"letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )

schedule.every().day.at("00:00").do(bDayWisher)

while True:
    schedule.run_pending()
    time.sleep(360) # wait for an hour
