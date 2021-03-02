import smtplib
import datetime as dt
import random
quotelist = []
date = dt.datetime.now()

with open("quotes.txt") as quote_data:
    quotelist = quote_data.read().splitlines()
print(quotelist)

email = ""
password = ""

if date.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="miltonicc@yahoo.com",
                            msg=f"Subject: Frase del lunes\n\nAca esta tu frase del lune: \n{random.choice(quotelist)}")
