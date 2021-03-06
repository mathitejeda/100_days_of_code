import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 0000 # Your latitude
MY_LONG = 0000  # Your longitude
EMAIL = ""
PASSWORD = ""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def check_position():
    if -5 <= (MY_LAT - iss_latitude) <= 5 and -5 <= (MY_LONG - iss_longitude) <= 5:
        return True

def send_email(from_email,to_email,password):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email,password=password)
        connection.sendmail(from_addr=from_email,to_addrs=to_email,msg="Subject: Look at the sky!\n\n Look at the sky, the iss may be close")
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
while True:
    if check_position() and sunset <= time_now.hour < sunrise:
        send_email(from_email=EMAIL,to_email="",password=PASSWORD)
    time.sleep(60)
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
