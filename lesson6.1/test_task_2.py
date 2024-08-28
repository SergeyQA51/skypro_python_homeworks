import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCalculator:
    @pytest.fixture(scope="class")
    def setup(self):
        print("Запуск веб-драйвера...")
        self.driver = webdriver.Chrome()  # Инициализация драйвера
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        yield self.driver  # Передаем self.driver через yield
        print("Закрытие веб-драйвера...")
        self.driver.quit()

    def testCalculator(self, setup):  # `setup` теперь передан напрямую
        print("Настройка задержки...")
        delayInput = setup.find_element(By.ID, "delay")  # Используем setup здесь
        delayInput.clear()
        delayInput.send_keys("45")

        print("Выполнение операции: 7 + 8...")
        setup.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
        setup.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']").click()
        setup.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']").click()
        setup.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

        print("Ожидание результата...")
        resultElement = WebDriverWait(setup, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")  # Ждем, пока результат будет '15'
        )

        result = setup.find_element(By.CLASS_NAME, "screen").text  # Получаем текст результата
        print(f"Полученный результат: {result}")
        assert result == "15", f"Результат должен быть '15', но получился '{result}'"



