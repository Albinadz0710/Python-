from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value):
        delay_input = self.wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, text):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']")))
        button.click()

    def get_result(self):
        screen = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        # Ждем, пока в поле не появится результат "15"
        self.wait.until(lambda d: screen.text == "15")
        return screen.text
    

    