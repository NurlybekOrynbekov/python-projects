import requests, bs4, os

url = 'https://www.xkcd.com'        # Начальный адрес
os.makedirs('xkcd', exist_ok=True)  # Папка загрузки комиксов

while not url.endswith('#'):
    # Загрузка старницы
    print('Загрузка страницы %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    # Поиск URL-адреса комикса
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображние комикса.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Загрузить изображение
        print('Загрузка изображения %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Сохранить изображения в папке ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Получение URL-адреса кнопки Prev
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://www.xkcd.com'+prevLink.get('href')
print('Готово.')