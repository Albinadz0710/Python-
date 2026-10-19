from selenium.webdriver.common.by import By

class ProductsListPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        # Ищем кнопку добавления в карточке нужного товара
        locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        