import datetime
import requests
from bs4 import BeautifulSoup

URL = 'https://tesis.lebedev.ru/magnetic_storms.html'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.41 YaBrowser/21.2.0.1097 Yowser/2.5 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    #r.encoding = 'utf8Bytes'
    return r


def get_cont(html):
    now = datetime.datetime.now()
    now = str(now)
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('b')

    a = items[2].getText()
    b = items[3].getText()
    c = items[4].getText()
    c1 = c[:1]
    c1 = int(c1)
    magnitude_level = ''

    if (c1<5) :
        magnitude_level = "Normal"
    if (c1>=5)&(c1<6) :
        magnitude_level = "G1"
    if (c1>=6)&(c1<7) :
        magnitude_level = "G2"
    if (c1 >= 7) & (c1 < 8):
        magnitude_level = "G3"
    if (c1>=8)&(c1<9) :
        magnitude_level = "G4"
    if  (c1>=9) :
        magnitude_level = "G5"
    f = open('info.txt', 'w')

    f.write("Today -")
    f.write( now  +'\n')
    f.write('Info from https://tesis.lebedev.ru/magnetic_storms.html'+'\n')

    f.write(a + '\n')
    f.write(b + '\n')
    f.write(c + '\n')

    print(magnitude_level)

def parse():
    html = get_html(URL)
    get_cont(html.text)


parse()