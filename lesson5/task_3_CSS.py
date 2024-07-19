from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

def run_test(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()  
    elif browser == 'firefox':
        driver = webdriver.Firefox() 
    
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/classattr")

        # Клик по кнопке с помощью локатора - Класс СSS
        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")  
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
