import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
NUTRI_ENDPOINT = ""
SHEETY_ENDPOINT = ""
SHEETY_TOKEN = ""

DATE = datetime.now().date().strftime("%d-%m-%Y")
TIME = datetime.now().now().strftime("%H:%M:%S")

exercise = input("What exercise did you do today?")
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
params = {
    "query": exercise,
    "gender": "",
    "weight_kg": "",
    "height_cm": "",
    "age": ""
}

nutri_response = requests.post(url=NUTRI_ENDPOINT, json=params, headers=header)
nutri_response.raise_for_status()
result = nutri_response.json()
exercise_data = nutri_response.json()["exercises"][0]

s_params = {
    "workout": {
        "date": DATE,
        "time": TIME,
        "exercise": exercise_data['user_input'],
        "duration": exercise_data['duration_min'],
        "calories": exercise_data['nf_calories']
    }
}

s_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

s_response = requests.post(url=SHEETY_ENDPOINT, json=s_params,headers=s_header)
print(s_response.json())
