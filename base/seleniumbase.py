from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    """
    Описывает общие методы работы selenium.webdrivewer с web элементами.
    spec. expected_conditions https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
    """

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 10)

    @staticmethod
    def __get_selenium_by(find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        """Visibility_of_element_located - Ожидание проверки того, что элемент присутствует в DOM объекта страница и видна.
        Видимость означает, что элемент не только отображается, но также имеет высоту и ширину, которые больше 0.
        Локатор - используется для поиска элемента возвращает WebElement, как только он будет найден и виден"""
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        """Visibility_of_element_located - Ожидание проверки того, что элемент присутствует в DOM объекта страница и видна.
        Видимость означает, что элемент не только отображается, но также имеет высоту и ширину, которые больше 0.
        Локатор - используется для поиска элемента возвращает WebElement, как только он будет найден и виден"""
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_visible(self, find_by: str, locator: str, locator_name=None) -> bool:
        """Visibility_of_element_located - Ожидание проверки того, что элемент присутствует в DOM объекта страница и видна.
        Видимость означает, что элемент не только отображается, но также имеет высоту и ширину, которые больше 0.
        Локатор - используется для поиска элемента возвращает WebElement, как только он будет найден и виден"""
        return self.__wait.until_not(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                     locator_name)

    #
    def to_be_clickable(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        """ Ожидание проверки элемента видно и включено, поэтому вы можете щелкнуть его.
        Элемент является либо локатором (текстом), либо WebElement"""
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        """ Ожидание проверки того, что все элементы присутствуют в DOM страницы и видимы.
        Видимость означает, что элементы не только отображаются, но также имеют высоту и ширину больше 0.
        локатор - используется для поиска элементов возвращает список WebElements, как только они будут обнаружены и видны """
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def find_element(self, find_by: str, locator: str) -> WebElement:
        """ Неявное ожидание"""
        return self.driver.find_element(self.__get_selenium_by(find_by), locator)

    def number_of_windows(self, num_windows: int) -> bool:
        return self.__wait.until(ec.number_of_windows_to_be(num_windows))
