from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase


class LocatorTensor(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.__block: str = '//*[text() = "{}"]/..'
        self.__link_block: str = '//*[text() = "{}"]/..//*[text() = "Подробнее"]'
        self.__image: str = '//*[contains(@class,"tensor_ru-About__block3-image-wrapper")]'

    def get_block(self, name: str) -> WebElement:
        """Получение WebElement блока по наименованию
                              (элемент присутствуют в DOM страницы и видим)"""
        return self.is_visible('xpath', self.__block.format(name), 'get_block')

    def get_link_block(self, name: str) -> WebElement:
        """Получение WebElement кнопки Подробнее в блоке
                              ((элемент виден и доступен для нажатия)"""
        return self.to_be_clickable('xpath', self.__link_block.format(name), 'get_link_block')

    def get_image(self) -> WebElement:
        """Получение всех WebElement изображений
                    (все элементы присутствуют в DOM страницы и видимы) """
        return self.are_visible('xpath', self.__image, 'get_image')
