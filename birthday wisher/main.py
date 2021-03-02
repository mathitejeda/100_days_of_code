import smtplib
import datetime as dt
import pandas
import random

letter_list = []
MAIL = input("Enter your mail")
PASSWORD = input("Enter your password")


def compare_birthday(day, month):
    now = dt.datetime.now()
    if now.day == day and now.month == month:
        return True
    else:
        return False


with open("letter_templates/letter_1.txt", mode="r") as letter:
    text = letter.read()
    letter_list.append(text)
with open("letter_templates/letter_2.txt", mode="r") as letter:
    text = letter.read()
    letter_list.append(text)
with open("letter_templates/letter_3.txt", mode="r") as letter:
    text = letter.read()
    letter_list.append(text)

print(letter_list)

birthdays_data = pandas.read_csv("birthdays.csv")
for (index, row) in birthdays_data.iterrows():
    if compare_birthday(day=row.day, month=row.month):
        msg = random.choice(letter_list).replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MAIL, to_addrs="miltonicc@yahoo.com", msg=f"Subject: Happy birthday\n\n{msg}")
