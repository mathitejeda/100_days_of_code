import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
page = response.text
soup = BeautifulSoup(page ,'html.parser')
movies = soup.find_all(class_='jsx-4245974604')
#the page now show the title via js so beautiful soup cannot find the title