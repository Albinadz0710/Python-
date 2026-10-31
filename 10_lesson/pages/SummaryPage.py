from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SummaryPage:
    """Класс, описывающий страницу подтверждения заказа (Summary)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы подтверждения заказа.

        :param driver: Экземпляр веб-драйвера Selenium.
        :type driver: WebDriver
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver = driver

    def get_total(self) -> str:
        """Получает итоговую сумму заказа со страницы.

        :return: Итоговая сумма в виде строки (например, "58.29").
        :rtype: str
        """
        # Получаем текст вида "Total: $58.29" и отрезаем всё лишнее, оставляя только число
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_text.replace("Total: $", "")

    