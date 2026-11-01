from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс, описывающий страницу корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы корзины.

        :param driver: Экземпляр веб-драйвера Selenium.
        :type driver: WebDriver
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """Нажимает кнопку оформления заказа (Checkout).

        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver.find_element(By.ID, "checkout").click()

