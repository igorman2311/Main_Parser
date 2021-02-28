
import requests
from bs4 import BeautifulSoup

URL = 'https://www.spaceweatherlive.com/ru.html'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.41 YaBrowser/21.2.0.1097 Yowser/2.5 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_cont(html):
    soup = BeautifulSoup(html, "html5lib")
    items = soup.find(lambda tag: tag.name == 'h4' and tag.get('class') == ['text-center'])



    print(items)


def parse():
    html = get_html(URL)
    get_cont(html.text)


parse()