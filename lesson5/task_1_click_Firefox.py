from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Инициализируем драйвер

Fdriver = webdriver.Firefox() 

try:
    # Открываем страницу
   
    Fdriver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    
    # Находим кнопку 'Add Element' и кликаем на нее 5 раз
  
    firefox_add_button = Fdriver.find_element(By.XPATH, "//button[text()='Add Element']")
    
    for _ in range(5):
    
        firefox_add_button.click()
        sleep(1)  

    # Собираем список кнопок 'Delete'
 
    firefox_delete_buttons = Fdriver.find_elements(By.XPATH, "//button[text()='Delete']")
    
    # Выводим размер списка

    print(f"Количество кнопок 'Delete': {len(firefox_delete_buttons)}")
    
finally:
    # Закрываем драйвер

    Fdriver.quit()