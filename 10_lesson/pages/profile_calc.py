from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс, описывающий страницу медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы калькулятора.

        :param driver: Экземпляр веб-драйвера Selenium.
        :type driver: WebDriver
        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """Открывает страницу калькулятора.

        :return: Ничего не возвращает.
        :rtype: None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value: int) -> None:
        """Устанавливает задержку (в секундах) в поле на странице.

        :param value: Значение задержки.
        :type value: int
        :return: Ничего не возвращает.
        :rtype: None
        """
        delay_input = self.wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, text: str) -> None:
        """Нажимает на кнопку калькулятора с указанным текстом.

        :param text: Текст на кнопке (например, "7", "+", "=").
        :type text: str
        :return: Ничего не возвращает.
        :rtype: None
        """
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']")))
        button.click()

    def get_result(self) -> str:
        """Ожидает и возвращает результат вычисления.

        :return: Текст результата на экране калькулятора.
        :rtype: str
        """
        # Ждем, пока на экране не появится текст "15"
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        result_element = self.driver.find_element(By.CLASS_NAME, "screen")
        return result_element.text

    
    

    