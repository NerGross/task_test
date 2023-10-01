import pytest


@pytest.mark.usefixtures('setup')
class Test:

    def test_first(self, sbis_fixture):
        """
        1) Перейти на https://sbis.ru/ в раздел "Контакты"
        2) Найти баннер Тензор, кликнуть по нему
        3) Перейти на https://tensor.ru/
        4) Проверить, что есть блок "Сила в людях"
        5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
        6) Находим раздел Работаем и проверяем, что у всех фотографии хронологии одинаковые высота (height) и ширина (width)
        """
        sbis_fixture.enter(self)
        sbis_fixture.first_script(self)

    def test_second(self, sbis_fixture):
        """
        1) Перейти на https://sbis.ru/ в раздел "Контакты"
        2) Проверить, что определился ваш регион (в нашем примере Ярославская обл.) и есть список партнеров.
        3) Изменить регион на Камчатский край
        4) Проверить, что подставился выбранный регион, список партнеров изменился, url и title содержат информацию выбранного региона
        """
        sbis_fixture.enter(self)
        sbis_fixture.second_script(self)

    def test_three(self, sbis_fixture):
        """
        1) Перейти на https://sbis.ru/
        2) В Footer'e найти и перейти "Скачать СБИС"
        3) Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом
        4) Убедиться, что плагин скачался
        5) Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте (в примере 3.64 МБ).
        """
        sbis_fixture.enter(self)
        sbis_fixture.third_script(self)
