import config
import re
import os.path
from time import sleep
from sbis.pages.locator_sbis import LocatorSbis
from sbis.pages.locator_ternsor import LocatorTensor
from base.utils import Utils
import logging
import allure

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.WARNING)
logger = logging.getLogger()


class Fixture:
    def __init__(self):
        self.driver = None

    @allure.feature("Тестовое_задание")
    @allure.story('Переход на https://sbis.ru/contacts')
    def enter(self):
        locator_sbis = LocatorSbis(self.driver)
        with allure.step("Переход на https://sbis.ru/ в раздел Контакты"):
            locator_sbis.get_header_menu("Контакты").click()
        with allure.step("Проверка, что в  title страницы присутствует Контакты"):
            assert "Контакты" in self.driver.title

    @allure.feature("Тестовое_задание")
    @allure.story('Первый сценарий')
    def first_script(self):
        locator_sbis = LocatorSbis(self.driver)
        locator_tensor = LocatorTensor(self.driver)
        with allure.step("Проверка, что открыто 1 окно"):
            assert len(self.driver.window_handles) == 1
        with allure.step("Поиск баннера Тензор, нажатие на него"):
            locator_sbis.get_banner().click()
        with allure.step("Ожидание, что количество окон станет равно 2"):
            locator_sbis.number_of_windows(2)
        with allure.step("Переход на https://tensor.ru/"):
            self.driver.switch_to.window(self.driver.window_handles[1])
        with allure.step("Проверка, что есть блок Сила в людях"):
            assert locator_tensor.get_block("Сила в людях")
        with allure.step("Переход в блоке Сила в людях в Подробнее"):
            self.driver.execute_script("arguments[0].click();", locator_tensor.get_link_block("Сила в людях"))
        with allure.step("Проверка, что открывается https://tensor.ru/about"):
            assert self.driver.current_url == config.URL_ABOUT
        with allure.step("Поиск раздела Работаем, получение размера фотографии хронологии"):
            Height = []
            Width = []
            for i in locator_tensor.get_image():
                Height.append(i.get_attribute('clientHeight'))
                Width.append(i.get_attribute('clientWidth'))
        with allure.step("Проверка, что у всех фотографии хронологии одинаковые высота (height) и ширина (width)"):
            for i in range(len(Height) - 1):
                assert Height[i] == Height[i + 1]
            for i in range(len(Width) - 1):
                assert Width[i] == Width[i + 1]

    @allure.feature("Тестовое_задание")
    @allure.story('Второй сценарий')
    def second_script(self):
        locator_sbis = LocatorSbis(self.driver)
        with allure.step("Проверка, что определился регион Ярославская обл."):
            assert locator_sbis.get_region_text() == 'Ярославская обл.'
        with allure.step("Проверка, что присутствует список партнеров"):
            partner = locator_sbis.get_partner()
            assert partner is not None
        with allure.step("Изменяем регион на Камчатский край"):
            locator_sbis.get_region().click()
            locator_sbis.get_button("Камчатский край").click()
        with allure.step("Проверка, что подставился выбранный регион"):
            sleep(1)
            assert locator_sbis.get_region_text() == "Камчатский край"
        with allure.step("Проверяем, что cписок партнеров изменился"):
            assert locator_sbis.get_partner() != partner
        with allure.step("Проверка, что title содержат информацию выбранного региона"):
            assert "Камчатский край" in self.driver.title
        with allure.step("Проверка, что url содержат информацию выбранного региона"):
            assert "kamchatskij-kraj" in self.driver.current_url

    @allure.feature("Тестовое_задание")
    @allure.story('Третий сценарий (необязательный)')
    def third_script(self):
        locator_sbis = LocatorSbis(self.driver)
        with allure.step("Поиск Скачать СБИС"):
            self.driver.execute_script("arguments[0].click();", locator_sbis.get_button("Скачать СБИС"))
        with allure.step("Переход в Скачать СБИС"):
            sleep(1)
            self.driver.execute_script("arguments[0].click();", locator_sbis.get_tab_button_download("СБИС Плагин"))
        with allure.step("Получение URL для загрузки"):
            href = locator_sbis.get_load_link().get_attribute('href')
        with allure.step("Получение имени загружаемого файла"):
            filename = href.split('/')[-1]
        with allure.step("Загрузка 'СБИС Плагин' для windows, веб-установщик в папку с данным тестом"):
            Utils.download(href, filename)
        with allure.step("Проверка, что плагин скачен"):
            assert os.path.exists(filename)
        with allure.step("Получение размера в байтах, перевод в МБ, округление до 2х знаков"):
            download_file = round(os.path.getsize(filename) / 1048576, 2)
        with allure.step("Получение из названия ссылки размер, перевод в str => float"):
            original_size = float('.'.join(re.findall(r'\d+', locator_sbis.get_load_link_text())))
        with allure.step("Загрузка размер скачанного файла в мегабайтах"):
            assert original_size == download_file
