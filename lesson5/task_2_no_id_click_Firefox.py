from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

# Функция для выполнения теста
def run_test(browser):
    
    if browser == 'firefox':
        driver = webdriver.Firefox()

    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")

        # Клик по синеей кнопке
        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
        blue_button.click()
        sleep(1) 
    finally:
        # Закрываем драйвер
        driver.quit()

# Запускаем тест 3 раза

for _ in range(3):
    print("Запуск теста в Firefox...")
    run_test('firefox')
    print("Тест завершен для Firefox.\n")