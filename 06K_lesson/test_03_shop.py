from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_byu(browser_firefox):
    wait = WebDriverWait(browser_firefox, 10)

    # 1. Откройте сайт магазина
    browser_firefox.get("https://www.saucedemo.com/")

    # 2. Авторизуйтесь
    user_name = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name")))
    user_name.clear()
    user_name.send_keys("standard_user")

    password = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
    password.clear()
    password.send_keys("secret_sauce")

    login = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))
    login.click()

    # 3. Добавьте товары в корзину
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))).click()

    # 4. Перейдите в корзину
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_link"))).click()

    # 5. Нажмите Checkout
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#checkout"))).click()

    # 6. Заполните форму
    first_name = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#first-name")))
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#last-name")))
    last_name.clear()
    last_name.send_keys("Иванов")

    postal_code = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#postal-code")))
    postal_code.clear()
    postal_code.send_keys("456789")

    # 7. Нажмите Continue
    btn_continue = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue")))
    btn_continue.click()

    # 8. Ищем итоговую стоимость
    total = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    summary = total.text
    price = summary.replace("Total: $", "").strip()
    assert price == "58.29", f"Ожидалось '58.29', но получено '{summary}'"
    print(f"✅ Тест пройден! Итоговая сумма: ${price}")
    
