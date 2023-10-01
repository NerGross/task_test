import requests


class Utils:
    """
       Описывает общие методы работы.
       """

    # Загрузка файла
    @staticmethod
    def download(url, filename):
        r = requests.get(url)
        if r.status_code == 200:
            with open(filename, "wb") as file:
                file.write(r.content)
        else:
            print('Ошибка при получении файла')
