from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    """Класс, описывающий страницу авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы.
        
        :param driver: Экземпляр веб-драйвера Selenium.
        :type driver: WebDriver
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver = driver

    def open(self) -> None:
        """Открывает главную страницу сайта.
        
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """Вводит логин, пароль и нажимает кнопку входа.
        
        :param username: Имя пользователя.
        :type username: str
        :param password: Пароль пользователя.
        :type password: str
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        