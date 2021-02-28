import datetime
import os
import requests
from bs4 import BeautifulSoup

#создае папку с текущей датой, с обработкой ошибки при попытки создания папки с одинаковым именем
try:
    now = datetime.datetime.now()
    dir1 = str(now)
    dir1 = dir1[0:10]
    os.mkdir(dir1) # #
except FileExistsError as e:
    pass
#создаем папку с текущей часом
dir2 = str(now.hour)
os.mkdir(dir1+"/"+dir2)
#дергаем картинку с коэф возумещния, скоростью солнечного ветра и тд
def kp_image(dir1, dir2):
    url = 'https://www.solarham.net/solarwind.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    img_tag = soup.find('img')
    photo_url = 'https://services.swpc.noaa.gov/images/geospace/geospace_3_hour.png'
    photo = requests.get(photo_url, headers=headers).content
    with open(dir1 + "/"+dir2+"/"+'Kp-index.png', 'wb') as f:
        f.write(photo)
#картинки со спутника СОХО
def soho_1(dir1, dir2):
    url = 'https://www.spaceweatherlive.com/ru/solnechnaya-aktivnost/izobrazheniya-solnca/soho.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    img_tag = soup.find('img')
    photo_url = 'https://sohowww.nascom.nasa.gov/data/realtime/c2/1024/latest.jpg'
    photo = requests.get(photo_url, headers=headers).content
    with open(dir1 + "/"+dir2+"/"+'soho_1.jpg', 'wb') as f:
        f.write(photo)
def soho_2(dir1, dir2):
    url = 'https://www.spaceweatherlive.com/ru/solnechnaya-aktivnost/izobrazheniya-solnca/soho.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    img_tag = soup.find('img')
    photo_url = 'https://sohowww.nascom.nasa.gov/data/realtime/c3/1024/latest.jpg'
    photo = requests.get(photo_url, headers=headers).content
    with open(dir1 + "/"+dir2+"/"+'soho_2.jpg', 'wb') as f:
        f.write(photo)
#еще картинки с того же сайта
def sdo_1(dir1, dir2):
    url = 'https://www.spaceweatherlive.com/ru/solnechnaya-aktivnost/izobrazheniya-solnca/sdo.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    img_tag = soup.find('img')
    photo_url = 'https://www.spaceweatherlive.com/images/SDO/SDO_HMIIF_512.jpg'
    photo = requests.get(photo_url, headers=headers).content
    with open(dir1 + "/"+dir2+"/"+'hmi.jpg', 'wb') as f:
        f.write(photo)
def sdo_2(dir1, dir2):
    url = 'https://www.spaceweatherlive.com/ru/solnechnaya-aktivnost/izobrazheniya-solnca/sdo.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    img_tag = soup.find('img')
    photo_url = 'https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0304.jpg'
    photo = requests.get(photo_url, headers=headers).content
    with open(dir1 + "/"+dir2+"/"+'304.jpg', 'wb') as f:
        f.write(photo)
def sdo_3(dir1, dir2):
    url = 'https://www.spaceweatherlive.com/ru/solnechnaya-aktivnost/izobrazheniya-solnca/sdo.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    img_tag = soup.find('img')
    photo_url = 'https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0131.jpg'
    photo = requests.get(photo_url, headers=headers).content
    with open(dir1 + "/"+dir2+"/"+'131.jpg', 'wb') as f:
        f.write(photo)

#вызываем по очереди все функции
kp_image(dir1,dir2)
soho_1(dir1,dir2)
soho_2(dir1,dir2)
sdo_1(dir1,dir2)
sdo_2(dir1,dir2)
sdo_3(dir1,dir2)

