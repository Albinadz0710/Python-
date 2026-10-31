from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsListPage:
    """Класс, описывающий страницу со списком товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы списка товаров.

        :param driver: Экземпляр веб-драйвера Selenium.
        :type driver: WebDriver
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """Добавляет указанный товар в корзину.

        :param product_name: Название товара, который нужно добавить.
        :type product_name: str
        :return: Ничего не возвращает.
        :rtype: None
        """
        # Ищем кнопку добавления в карточке нужного товара
        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button",
        )
        self.driver.find_element(*locator).click()

    def go_to_cart(self) -> None:
        """Кликает по иконке корзины для перехода на страницу корзины.

        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
            