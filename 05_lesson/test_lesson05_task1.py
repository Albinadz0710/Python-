from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_navigation():
    print("2. Запуск функции test_navigation")
    driver = webdriver.Chrome()
    
    try:
    
        base_url = "https://httpbin.qa-territory.online"
        print("3. Открываем страницу:", base_url)
        driver.get(base_url)
    
    
        initial_url = driver.current_url.rstrip('/')
        print(f"4. Текущий URL (очищенный): {initial_url}")

    
        print('5. Ищем ссылку "HTML Form"')
        html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
        print("6. Кликаем по ссылке")
        html_form_link.click()

        time.sleep(1) 

    
        expected_path = "/forms/post"
        current_url_after_click = driver.current_url.rstrip('/')
        assert current_url_after_click.endswith(expected_path), (
            f"Ошибка навигации вперед: ожидался путь '{expected_path}', "
            f"получен '{current_url_after_click}'"
        )
        print("7. Проверка URL пройдена")

    
        print("9. Возвращаемся назад")
        driver.back()

        time.sleep(1)

    
        returned_url = driver.current_url.rstrip('/')
        print(f"10. URL после возврата (очищенный): {returned_url}")
        
        
        assert returned_url == initial_url, (
            f"Ошибка возврата назад: ожидался URL '{initial_url}', "
            f"получен '{returned_url}'"
        )
        print("8. Проверка возврата пройдена ✅")
        
    except AssertionError as e:
        print(f"❌ Тест упал: {e}")
        raise  
    finally:
        print("12. Закрываем браузер")
        driver.quit()
        print("13. Браузер закрыт")



if __name__ == "__main__":
    print("1. Начало выполнения скрипта")
    print("14. Запуск main")
    test_navigation()

