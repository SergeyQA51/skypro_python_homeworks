from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Инициализируем драйвер
Cdriver = webdriver.Chrome()

try:
    # Открываем страницу
    Cdriver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    
    # Находим кнопку 'Add Element' и кликаем на нее 5 раз
    chrome_add_button = Cdriver.find_element(By.XPATH, "//button[text()='Add Element']")
    
    for _ in range(5):
        chrome_add_button.click()
        sleep(1)  

    # Собираем список кнопок 'Delete'
    chrome_delete_buttons = Cdriver.find_elements(By.XPATH, "//button[text()='Delete']")
   
    # Выводим размер списка
    print(f"Количество кнопок 'Delete': {len(chrome_delete_buttons)}")
    
finally:
    # Закрываем драйвер
    Cdriver.quit()