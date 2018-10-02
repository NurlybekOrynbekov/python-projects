# -*- coding: utf-8 -*-
import requests, bs4, os
import threading
import re

url = 'https://www.xkcd.com'        # Начальный адрес
os.makedirs('xkcd', exist_ok=True)  # Папка загрузки комиксов
os.makedirs('xkcd-logs', exist_ok=True)
skipComicks = ['404', '1416']

def thread(func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper

@thread
def download(startPage, endPage, threadNum):
    filename = 'xkcd-logs/log-' + str(threadNum) + '.txt'
    f = open(filename, 'w')
    print('Thread ' + str(threadNum) + ' start.')
    f.write('Thread ' + str(threadNum) + ' start.\n')
    for x in range(startPage, endPage):
        try:
            if x in skipComicks:
                continue
            link = 'https://www.xkcd.com/' + str(x)
            # Загрузка старницы
            print('Loading page %s...' % link)
            f.write('Loading page %s...\n' % link)
            res = requests.get(link)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text)

            # Поиск URL-адреса комикса
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Can\'t find image - ' + link)
                f.write('Can\'t find image - ' + link + '\n')
            else:
                comicUrl = 'https:' + comicElem[0].get('src')
                # Загрузить изображение
                print('Dowload image %s...' % (comicUrl))
                f.write('Dowload image %s...\n' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()

                # Сохранить изображения в папке ./xkcd
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
        except Exception:
            print('Error in comicUrl - ' + comicUrl)
            f.write('Error int comicUrl - ' + comicUrl + '\n')
        
    print('Thread ' + str(threadNum) + ' end work.')
    f.write('Thread ' + str(threadNum) + ' end work.\n')
    f.close()

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
prevLink = soup.select('a[rel="prev"]')[0]
comics = int(re.search(r'\d+', prevLink.get('href')).group(0)) + 1
print(comics)
n = int(input('Threads: '))
avg = int(comics/n)
o = int(comics%n)
print(avg)
print(o)

for x in range(n):
    y = x + 1
    startPage = y * avg + 1
    endPage = (y + 1) * avg
    if y == n:
        download(startPage, endPage + o, y)
    else:
        download(startPage, endPage, y)