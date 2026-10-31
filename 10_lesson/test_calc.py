import allure
from selenium import webdriver
from pages.profile_calc import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка работы медленного калькулятора (7 + 8 = 15)")
@allure.description("Тест проверяет, что калькулятор корректно выполняет сложение с задержкой 45 секунд.")
def test_calculator():
    driver = webdriver.Chrome()
    try:
        with allure.step("Открыть страницу калькулятора"):
            page = CalculatorPage(driver)
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Выполнить сложение: 7 + 8"):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Проверить результат вычисления"):
            result = page.get_result()
            
            with allure.step(f"Проверить, что результат равен 15 (фактический: {result})"):
                assert result == "15", f"Ожидался результат 15, но получен {result}"
    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()    

            