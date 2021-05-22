import requests
import time
import datetime


def main():
    download_count = 100  # Кол-во картинок для скачивания
    path = 'E:\Images'  # Путь в директорию, куда сохранять картинки
    for i in range(download_count):
        response = requests.get('https://thispersondoesnotexist.com/image')
        nowtime = datetime.datetime.now()
        imagename = nowtime.strftime("%Y%m%d%H%M%S")
        image = open(f'{path}\img{imagename}.jpg', 'wb')
        image.write(response.content)
        image.close()
        if i % 10 == 0:
            print(f'{100 * i / download_count}%')
        time.sleep(0.5)


if __name__ == '__main__':
    main()
