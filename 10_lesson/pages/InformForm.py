from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutFormPage:
    """Класс, описывающий страницу заполнения формы оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы формы.

        :param driver: Экземпляр веб-драйвера Selenium.
        :type driver: WebDriver
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        """Заполняет поля формы данными пользователя и нажимает Continue.

        :param first_name: Имя пользователя.
        :type first_name: str
        :param last_name: Фамилия пользователя.
        :type last_name: str
        :param zip_code: Почтовый индекс.
        :type zip_code: str
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

        