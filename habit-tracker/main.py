import requests

pixela_endpoint = "https://pixe.la/v1/users"
USER = ""
TOKEN = ""


params = {
    "token":TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint,json=params)
# print(response.text)

graph_endpoint =