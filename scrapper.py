from bs4 import BeautifulSoup
import requests
from requests.models import ContentDecodingError
import parser
market_watch_url = "https://www.marketwatch.com/column/the-fed?mod=side_nav"
r1 = requests.get(market_watch_url)
coverpage = r1.content

soup = BeautifulSoup(coverpage, 'html.parser')

headlines = soup.find_all(class_="article__headline")
headlines_list = list()
for headline in headlines:
    headlines_list.append(headline.get_text().strip())

business_insider_url = "https://www.businessinsider.com/s?q=fed"
r = requests.get(business_insider_url).content
soup = BeautifulSoup(r, 'html.parser')
headlines = soup.find_all(class_="tout-title-link")
headlines_list = list()
for headline in headlines:
    headlines_list.append(headline.get_text().strip())

for i in headlines_list:
    print(i)
    print("\n")