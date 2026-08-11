from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    
    try:

        driver.get("https://httpbin.qa-territory.online/forms/post")
        original_url = driver.current_url
        print(f"Исходный URL: {original_url}")


        name_field = driver.find_element(By.NAME, "custname")
        name_field.send_keys("Альбина")
        print("Имя введено успешно")


        submit_button = driver.find_element(By.XPATH, "//*[contains(translate(text(), 'SUBMIT', 'submit'), 'submit')]")
        submit_button.click()
        print("Кнопка Submit нажата")


        new_url = driver.current_url
        print(f"Новый URL: {new_url}")


        assert new_url != original_url, "URL не изменился после отправки формы"
        
        print("✅ Тест пройден: URL изменился после отправки формы")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_form_submission()
    
