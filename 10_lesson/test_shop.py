import allure
from selenium import webdriver
from pages.Authorization import LoginPage
from pages.ProductsList import ProductsListPage
from pages.CardShop import CartPage
from pages.InformForm import CheckoutFormPage
from pages.SummaryPage import SummaryPage

@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Сквозной тест: покупка трех товаров")
@allure.description("Проверяет полный путь пользователя: авторизация, добавление трех товаров в корзину, оформление заказа и проверка итоговой суммы.")
def test_shop():
    driver = webdriver.Firefox()
    try:
        with allure.step("1. Авторизация на сайте"):
            login = LoginPage(driver)
            login.open()
            login.login("standard_user", "secret_sauce")

        with allure.step("2. Добавление трех товаров в корзину"):
            products = ProductsListPage(driver)
            products.add_to_cart("Sauce Labs Backpack")
            products.add_to_cart("Sauce Labs Bolt T-Shirt")
            products.add_to_cart("Sauce Labs Onesie")
        
        with allure.step("3. Переход в корзину и нажатие Checkout"):
            products.go_to_cart()
            cart = CartPage(driver)
            cart.click_checkout()

        with allure.step("4. Заполнение формы доставки"):
            form = CheckoutFormPage(driver)
            form.fill_form("Ivan", "Ivanov", "123456")

        with allure.step("5. Проверка итоговой суммы заказа"):
            summary = SummaryPage(driver)
            total = summary.get_total()
            
            # Выделяем проверку в отдельный шаг
            with allure.step(f"Проверяем, что сумма равна 58.29 (фактическая: {total})"):
                assert total == "58.29", f"Ожидалась сумма 58.29, но получена {total}"
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()

            
        