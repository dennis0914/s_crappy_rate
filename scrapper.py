from bs4 import BeautifulSoup
import requests
from requests.models import ContentDecodingError


def scrape():
    market_watch = "https://www.marketwatch.com/column/the-fed?mod=side_nav"
    business_insider = "https://www.businessinsider.com/s?q=fed"
    yahoo = "https://news.search.yahoo.com/search?p=the+fed&fr=uh3_news_vert_gs&fr2=p%3Anews%2Cm%3Asb"
    bing = "https://www.bing.com/news/search?q=the+fed&qft=interval%3d%228%22+sortbydate%3d%221%22&form=NWRFSH"

    headlines_list = list()

    scrape_target={
        bing: {'target': '_blank', 'class': 'title'},
        market_watch: {'class': 'article__headline'},
        business_insider: {'class': 'tout-title-link'},
        yahoo: {'style': 'font-size:16px;', 'referrerpolicy': 'unsafe-url'}
        }

    for key, value in scrape_target.items():
        r = requests.get(key, headers = {"Accept-Language": "en-US"}).content
        soup = BeautifulSoup(r, 'html.parser')
        headlines = soup.find_all(attrs=value)
        for headline in headlines:
            #drop if headline is not in english
            try:
                headline.get_text().strip().encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                continue
            else:
                headlines_list.append(headline.get_text().strip())

    return headlines_list