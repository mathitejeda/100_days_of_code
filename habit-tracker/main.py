import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER = ""
TOKEN = ""

params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=params)
# print(response.text)

# graph_params = {
#     "id": "",
#     "name": "",
#     "unit": "",
#     "type": "",
#     "color": "",
# }
#
headers = {
    "X-USER-TOKEN": TOKEN,
}
#
# graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USER}/graphs/<graph>"

today = datetime(day=15, month=3, year=2021)

post_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120",
}

response = requests.post(url=post_endpoint, json=post_body, headers=headers)

# update_endpoint = f"{pixela_endpoint}/{USER}/graphs/<graph>/20210315"
#
# response = requests.put(url=update_endpoint,json=post_body,headers=headers)
# print(response.text)
