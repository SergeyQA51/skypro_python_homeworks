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
        driver.get("http://the-internet.herokuapp.com/entry_ad")
        
        sleep(3)
        
        # Находим кнопку Close в модальном окне и кликаем на нее
        close_button = driver.find_element(By.XPATH, "//div[@class='modal']/div[@class='modal-footer']/p[contains(text(),'Close')]/..")
        close_button.click()
        
        sleep(1) 

    finally:
        # Закрываем драйвер
        driver.quit()

# Запускаем тест для Chrome
print("Запуск теста в Chrome...")
run_test('chrome')
print("Тест завершен для Chrome.\n")

# Запускаем тест для Firefox
print("Запуск теста в Firefox...")
run_test('firefox')
print("Тест завершен для Firefox.\n")