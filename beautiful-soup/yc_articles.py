from bs4 import BeautifulSoup
import requests

# with open('website.html',encoding='utf-8') as html_file: # encoding is a way to patch an error lol
#     content = html_file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)

response = requests.get('https://news.ycombinator.com/')
webpage = response.text
soup = BeautifulSoup(webpage,'html.parser')

first_article = soup.find_all(name='a', class_='storylink')

fa_text = [article.text for article in first_article]
fa_link = [article.get('href') for article in first_article]
fa_score = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]

max_score_index = fa_score.index(max(fa_score))
print(fa_text[max_score_index])
print(fa_link[max_score_index])
print(fa_score[max_score_index])
