import requests
from twilio.rest import Client

api_key = ""
auth_token = ""
acc_sid = ""

params = {
    "lat": -32.897621,
    "lon": -60.688808,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data = response.json()["hourly"][:11]
condition_codes = [element["weather"][0]["id"] for element in data]

will_rain = False

for code in condition_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(acc_sid,auth_token)
    message = client.messages \
        .create(
        body="It will rain today, use an umbrella",
        from_='',
        to=''
    )
    print(message.status)