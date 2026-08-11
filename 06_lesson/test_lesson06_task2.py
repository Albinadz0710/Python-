from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    # Создаем драйвер внутри функции
    driver = webdriver.Chrome()
    
    try:
        # 1. Откройте страницу https://gitflic.ru/
        driver.get("https://gitflic.ru/")

        # 2. Установите cookie пользователя 1.
        driver.add_cookie(
            {
                "name": "SESSION",
                "value": "NDkwZDE5ZjYtNzI5Yy00NjFhLWJiNDYtNGUxNGZlOTAwOTNj",
                "domain": ".gitflic.ru",
                "path": "/"
            }
        )

        # Добавляем cookie для окна подтверждения работы с cookie
        driver.add_cookie(
            {
                "name": "cookiesAccepted",
                "value": "true",
                "domain": ".gitflic.ru",
                "path": "/"
            }
        )

        # 3. Обновляем страницу, чтобы cookie применилась
        driver.refresh()

        # 4. Перейдите на страницу пользователя 1.
        driver.get("https://gitflic.ru/user/xoziaka")

        # 5. Сохраните текущий URL.
        url1 = driver.current_url
        print(f"URL пользователя 1: {url1}")

        # 6. Разлогиньтесь (очистите куки).
        driver.delete_all_cookies()

        # 7. Установите cookie пользователя 2.
        driver.add_cookie(
            {
                "name": "SESSION",
                "value": "MjE4OTllNjAtMTJhZC00OWFkLTk2YTItNThhMjUzYWYxMjE1",
                "domain": ".gitflic.ru",
                "path": "/"
            }
        )

        # Добавляем cookie для окна подтверждения работы с cookie
        driver.add_cookie(
            {
                "name": "cookiesAccepted",
                "value": "true",
                "domain": ".gitflic.ru",
                "path": "/"
            }
        )

        # 8. Обновляем страницу, чтобы cookie применилась
        driver.refresh()

        # 9. Перейдите на страницу пользователя 2.
        driver.get("https://gitflic.ru/user/user21")

        # 10. Сохраните текущий URL.
        url2 = driver.current_url
        print(f"URL пользователя 2: {url2}")

        # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
        assert url1 != url2, f"URL совпадают: {url1}"
        print("Тест пройден!")
        
    finally:
        driver.quit()

# ВЫЗЫВАЕМ ФУНКЦИЮ
if __name__ == "__main__":
    test_session_storage_auth()

