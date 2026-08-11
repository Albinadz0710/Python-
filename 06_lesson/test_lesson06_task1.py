from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    
    try:
        # 1. Откройте страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        print("Страница загружена")

        # 2. Найдите и нажмите на кнопку "Start"
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()
        print("Кнопка Start нажата")

        # 3. Дождитесь появления текста "Hello World!"
        hello_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        print("Текст Hello World! появился")

        # 4. Сделайте скриншот страницы
        driver.save_screenshot("dynamic_loading_screenshot.png")
        print("Скриншот сохранен как 'dynamic_loading_screenshot.png'")

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        actual_text = hello_element.text
        expected_text = "Hello World!"
        assert actual_text == expected_text, \
            f"Ожидался текст '{expected_text}', получен '{actual_text}'"
        print(f"✅ Текст совпадает: '{actual_text}'")

        print("✅ Тест пройден успешно!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()
    
