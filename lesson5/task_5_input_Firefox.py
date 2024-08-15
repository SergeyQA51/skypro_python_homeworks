from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

def run_test(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()  
    
    try:
# Переход на страницу
        driver.get("http://the-internet.herokuapp.com/inputs")
        
        sleep(2)
        
# Находим поле ввода
        input_field = driver.find_element(By.TAG_NAME, "input")
        
# Вводим текст 1000
        input_field.send_keys("1000")
        sleep(1)
        
# Очищаем поле ввода
        input_field.clear()
        sleep(1)  
        
# Вводим текст 999
        input_field.send_keys("999")
        sleep(1) 
    finally:
# Закрываем драйвер
        driver.quit()

# Запускаем тест для Firefox
print("Запуск теста в Firefox...")
run_test('firefox')
print("Тест завершен для Firefox.\n")