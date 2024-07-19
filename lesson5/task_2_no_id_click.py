from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

# Функция для выполнения теста
def run_test(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()

    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")

        # Клик по синеей кнопке
        blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
        blue_button.click()
        sleep(1) 
    finally:
        # Закрываем драйвер
        driver.quit()

# Запускаем тест 3 раза для каждого браузера
for _ in range(3):
    print("Запуск теста в Chrome...")
    run_test('chrome')
    print("Тест завершен для Chrome.\n")

for _ in range(3):
    print("Запуск теста в Firefox...")
    run_test('firefox')
    print("Тест завершен для Firefox.\n")

