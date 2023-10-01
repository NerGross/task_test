from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase


class LocatorSbis(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.__header_menu: str = '//*[contains(@class,"Header")]/*[text()="{}"]'
        self.__button: str = '//*[contains(text(), "{}")]'
        self.__banner: str = '//*[contains(@class,"sbisru-Contacts__logo-tensor mb-12")]'
        self.__partner: str = '//*[contains(@class,"sbisru-Contacts-List__col-1")]'
        self.__region: str = '//*[contains(@class,"Region-Chooser ml-16")]/span'
        self.__tab_button_download: str = '//*[(@class = "controls-TabButton__caption") and (text() = "{}")]'
        self.__load_link: str = '//*[contains( @ href,"web")]'

    def get_header_menu(self, name: str) -> WebElement:
        """Получение WebElement кнопки в панели навигации по названию
            (элемент виден и доступен для нажатия)"""
        return self.to_be_clickable('xpath', self.__header_menu.format(name), 'get_header_menu')

    def get_button(self, name: str) -> WebElement:
        """Получение WebElement кнопки по названию
            (элемент виден и доступен для нажатия)"""
        return self.to_be_clickable('xpath', self.__button.format(name), 'get_button')

    def get_banner(self) -> WebElement:
        """Получение WebElement баннера
            (элемент виден и доступен для нажатия)"""
        return self.to_be_clickable('xpath', self.__banner, 'get_banner')

    def get_region(self) -> WebElement:
        """Получение WebElement региона
            (элемент виден и доступен для нажатия)"""
        return self.to_be_clickable('xpath', self.__region, 'get_region')

    def get_region_text(self) -> str:
        """Получение наименования WebElement региона"""
        return self.get_region().text

    def get_partner(self) -> WebElement:
        """Получение всех WebElement блока партнеры
            (все элементы присутствуют в DOM страницы и видимы) """
        return self.are_visible('xpath', self.__partner, 'get_partner')

    def get_tab_button_download(self, name: str) -> WebElement:
        """Получение WebElement меню навигации страницы "Скачать" по названию
            (элемент виден и доступен для нажатия)"""
        return self.to_be_clickable('xpath', self.__tab_button_download.format(name), 'get_tab_button_download')

    def get_load_link(self) -> WebElement:
        """Получение WebElement ссылки на скачивания
                      (элемент присутствуют в DOM страницы и видим)"""
        return self.is_visible('xpath', self.__load_link, 'get_load_link')

    def get_load_link_text(self) -> str:
        """Получение наименования WebElement ссылки на скачивания"""
        return self.get_load_link().text
