from selenium.webdriver.common.by import By

class SummaryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total(self):
        # Получаем текст вида "Total: $58.29" и отрезаем всё лишнее, оставляя только число
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_text.replace("Total: $", "")

    