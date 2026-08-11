from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    
    try:
    
        driver.get("https://httpbin.qa-territory.online/links/10")
        print(f"Открыта страница: {driver.current_url}")
    
    
        links = driver.find_elements(By.TAG_NAME, "a")
    
    
        expected_count = 9
        actual_count = len(links)
        assert actual_count == expected_count, \
            f"Ожидалось {expected_count} ссылок, найдено {actual_count}"
        print(f"✅ Найдено {actual_count} ссылок")
    
    
        for i, link in enumerate(links, 1):
            assert link.is_displayed(), f"Ссылка #{i} не отображается на странице"
        print("✅ Все ссылки отображаются")
    

        first_link_text = links[0].text
        assert "1" in first_link_text, \
            f"Текст первой ссылки '{first_link_text}' не содержит '1'"
        print(f"✅ Текст первой ссылки содержит '1': '{first_link_text}'")
    
        print("✅ Все проверки пройдены успешно!")
    
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_multiple_elements()
