import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
    
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
# Вводим значение 45 в поле ввода
delay_input = driver.find_element(By.ID, "delay")
# Удаляем стоковое значение при загрузке сайта
delay_input.clear()
delay_input.send_keys("45")
    
# Нажимаем кнопки: 7, +, 8, =
driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']").click()
driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']").click()
driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()
   
# ставим 46 секунд для отображения результата и его считывания
time.sleep(46)

# Проверяем результат
result = driver.find_element(By.CLASS_NAME, "screen").text
assert result == "15", f"Результат должен быть '15', но получился '{result}'"
print(f"Полученный результат: {result}")

driver.quit()