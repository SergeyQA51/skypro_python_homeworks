import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_number(self, number):
        self.driver.find_element(By.XPATH, f"//span[@class='btn btn-outline-primary' and text()='{number}']").click()

    def click_operator(self, operator):
        self.driver.find_element(By.XPATH, f"//span[@class='operator btn btn-outline-success' and text()='{operator}']").click()

    def click_equals(self):
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

    def get_result(self):
        return WebDriverWait(self.driver, 45).until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen"))
        ).text

class TestCalculator:
    @pytest.fixture(scope="class")
    def setup(self):
        print("Запуск веб-драйвера...")
        self.driver = webdriver.Chrome()  # Инициализация драйвера
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield self.driver  # Передаем self.driver через yield
        print("Закрытие веб-драйвера...")
        self.driver.quit()

    def test_calculator(self, setup):  # setup теперь передан напрямую
        calculator_page = SlowCalculatorPage(setup)  # Создаем объект страницы

        print("Настройка задержки...")
        calculator_page.set_delay("45")

        print("Выполнение операции: 7 + 8...")
        calculator_page.click_number(7)
        calculator_page.click_operator('+')
        calculator_page.click_number(8)
        calculator_page.click_equals()

        
        print("Ожидание результата...")
        resultElement = WebDriverWait(setup, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")  # Ждем, пока результат будет '15'
        )
        result = calculator_page.get_result()  # Получаем текст результата
        print(f"Полученный результат: {result}")

        assert result == "15", f"Результат должен быть '15', но получился '{result}'"
