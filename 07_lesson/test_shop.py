from selenium import webdriver
from pages.Authorization import LoginPage
from pages.ProductsList import ProductsListPage
from pages.CardShop import CartPage
from pages.InformForm import CheckoutFormPage
from pages.SummaryPage import SummaryPage

def test_shop():
    driver = webdriver.Firefox()
    try:
        # 1. Авторизация
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        # 2. Добавление товаров
        products = ProductsListPage(driver)
        products.add_to_cart("Sauce Labs Backpack")
        products.add_to_cart("Sauce Labs Bolt T-Shirt")
        products.add_to_cart("Sauce Labs Onesie")
        
        # 3. Переход в корзину и Checkout
        products.go_to_cart()
        cart = CartPage(driver)
        cart.click_checkout()

        # 4. Заполнение формы
        form = CheckoutFormPage(driver)
        form.fill_form("Ivan", "Ivanov", "123456")

        # 5. Проверка суммы
        summary = SummaryPage(driver)
        total = summary.get_total()
        assert total == "58.29"
    finally:
        driver.quit()

        