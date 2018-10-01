import requests, bs4, os
import threading
import re

url = 'https://www.xkcd.com'        # Начальный адрес
os.makedirs('xkcd', exist_ok=True)  # Папка загрузки комиксов

def thread(func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper

@thread
def download(startPage, endPage, threadNum):
    filename = 'log-' + str(threadNum) + '.txt'
    f = open(filename, 'w')
    print('Поток ' + str(threadNum) + ' стартовал.')
    f.write('Поток ' + str(threadNum) + ' стартовал.')
    for x in range(startPage, endPage):
        try:
            if x == 404:
                continue
            link = 'https://www.xkcd.com/' + str(x)
            # Загрузка старницы
            print('Загрузка страницы %s...' % link)
            f.write('Загрузка страницы %s...' % link)
            res = requests.get(link)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text)

            # Поиск URL-адреса комикса
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Не удалось найти изображние комикса - ' + link)
                f.write('Не удалось найти изображние комикса - ' + link)
            else:
                comicUrl = 'https:' + comicElem[0].get('src')
                # Загрузить изображение
                print('Загрузка изображения %s...' % (comicUrl))
                f.write('Загрузка изображения %s...' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()

                # Сохранить изображения в папке ./xkcd
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
        except Exception:
            print('Ошибка на comicUrl - ' + comicUrl)
            f.write('Ошибка на comicUrl - ' + comicUrl)
        
    print('Поток ' + str(threadNum) + ' Закончил работу.')
    f.write('Поток ' + str(threadNum) + ' Закончил работу.')
    f.close()

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
prevLink = soup.select('a[rel="prev"]')[0]
comics = int(re.search(r'\d+', prevLink.get('href')).group(0))
print(comics)
n = int(input('Количество потоков: '))
avg = int(comics/n)
o = comics%n
print(avg)
print(o)

for x in range(n):
    y = x + 1
    if y == n:
        download(((y - 1) * avg) + 1, y * avg + o, y)
    else:
        download(((y - 1) * avg) + 1, y * avg, y)