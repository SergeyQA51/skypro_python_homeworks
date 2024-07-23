from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

# Функция для выполнения теста
def run_test(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    

    try:
        # Открываем страницу
        driver.get("http://the-internet.herokuapp.com/login")
        
        sleep(2)
        
        # Находим поле username и вводим значение
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys("tomsmith")

        sleep(1)
        
        # Находим поле password и вводим значение
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("SuperSecretPassword!")
        
        sleep(1)
        
        # Находим кнопку Login и нажимаем на нее
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        sleep(2)
    finally:
        # Закрываем драйвер
        driver.quit()

# Запускаем тест для Chrome
print("Запуск теста в Chrome...")
run_test('chrome')
print("Тест завершен для Chrome.\n")

