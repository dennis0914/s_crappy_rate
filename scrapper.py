from bs4 import BeautifulSoup
import requests
from requests.models import ContentDecodingError
import parser
url = "https://www.marketwatch.com/column/the-fed?mod=side_nav"
r1 = requests.get(url)
coverpage = r1.content

soup = BeautifulSoup(coverpage, 'html.parser')

headlines = soup.find_all(class_="article__headline")
headlines_list = list()
for headline in headlines:
    headlines_list.append(headline.get_text().strip())

print(headlines_list[3])