from bs4 import BeautifulSoup
import requests

date= input('which year would you like to travel(yyyy-mm-dd): ')
billboard = []
url = f'https://www.billboard.com/charts/hot-100/{date}'
response = requests.get(url=url)
soup = BeautifulSoup(response.text,'html.parser')
billboard = soup.findAll('span',class_="chart-element__information__song text--truncate color--primary")
billboard = [song.getText() for song in billboard]
print(billboard)
