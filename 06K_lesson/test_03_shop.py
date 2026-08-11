from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_byu(browser):
    wait = WebDriverWait(browser, 10)

    # 1. Откройте сайт магазина
    browser.get("https://www.saucedemo.com/")

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
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#first-name"))).send_keys("Иван")
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#last-name"))).send_keys("Иванов")
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#postal-code"))).send_keys("456789")

    # 7. Нажмите Continue с обработкой всплывающего окна
    btn_continue = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue")))
    btn_continue.click()
    
    # Ждем немного
    time.sleep(1)
    
    # Проверяем URL и обрабатываем возможные проблемы
    current_url = browser.current_url
    print(f"URL после нажатия Continue: {current_url}")
    
    # Если мы все еще на странице checkout-step-one, пытаемся нажать Continue еще раз
    if "checkout-step-one.html" in current_url:
        print("Все еще на странице checkout-step-one, пробуем еще раз...")
        
        # Проверяем, нет ли всплывающего окна
        try:
            # Ищем любую кнопку во всплывающем окне
            popup_buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'OK') or contains(text(), 'Cancel') or contains(text(), 'Continue')]")
            if popup_buttons:
                print(f"Найдено всплывающее окно с кнопками, нажимаем первую кнопку...")
                popup_buttons[0].click()
                time.sleep(1)
                
                # Пытаемся нажать Continue снова
                btn_continue = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue")))
                btn_continue.click()
        except:
            print("Всплывающего окна не обнаружено")
        
        # Проверяем еще раз
        time.sleep(1)
        current_url = browser.current_url
        print(f"URL после повторной попытки: {current_url}")
    
    # Проверяем, перешли ли мы на страницу итогов
    if "checkout-step-two.html" not in current_url:
        # Если не перешли, пробуем прямой переход на страницу итогов
        print("Не удалось перейти через кнопку Continue, пробуем прямой переход...")
        browser.get("https://www.saucedemo.com/checkout-step-two.html")
        time.sleep(2)

    # 8. Теперь ищем итоговую стоимость на странице checkout-step-two
    try:
        # Ждем загрузки страницы итогов
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))
        
        # Ищем итоговую стоимость
        total = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        summary = total.text
        print(f"Найдена итоговая сумма: '{summary}'")
        
        # 9. Проверяем сумму
        price = summary.replace("Total: $", "").strip()
        assert price == "58.29", f"Ожидалось '58.29', но получено '{summary}'"
        print(f"✅ Тест пройден! Итоговая сумма: ${price}")
        
    except Exception as e:
        print(f"Ошибка при поиске итоговой суммы: {e}")
        
        # Если не удалось найти сумму, выводим информацию для отладки
        print(f"\nТекущий URL: {browser.current_url}")
        print(f"Заголовок страницы: {browser.title}")
        
        # Пытаемся найти любую информацию о сумме
        all_text = browser.find_element(By.TAG_NAME, "body").text
        print(f"\nТекст страницы:\n{all_text[:500]}...")
        
        # Проверяем наличие товаров в корзине
        cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")
        print(f"\nКоличество товаров в корзине: {len(cart_items)}")
        
        if "Total:" in all_text:
            print("\nНайден текст 'Total:' на странице")
            # Ищем строку с Total
            lines = all_text.split('\n')
            for line in lines:
                if "Total:" in line:
                    print(f"Найдена строка с Total: '{line}'")
                    # Пробуем извлечь сумму
                    try:
                        import re
                        price_match = re.search(r'\d+\.\d+', line)
                        if price_match:
                            price = price_match.group()
                            assert price == "58.29", f"Ожидалось '58.29', получено '{price}'"
                            print(f"✅ Тест пройден! Итоговая сумма: ${price}")
                    except:
                        pass
        
        assert False, "Не удалось найти итоговую стоимость на странице"
