import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

wait = WebDriverWait(driver, 30)  
try:
    print("Ожидание элемента...")
    ajax_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bg-success")))  
    print("Элемент найден!")
    text = ajax_content.text
    print(text)
except TimeoutException:
    print("Элемент не найден в течение указанного времени.")
    
finally:

    driver.quit()