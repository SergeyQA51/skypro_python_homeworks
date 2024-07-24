from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

service = Service('path/to/chromedriver')
driver = webdriver.Chrome()

try:
    # Шаг 1: Открыть страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    
    # Шаг 2: Заполнить форму
    driver.find_element(By.NAME, "first-name").send_keys('Иван')
    driver.find_element(By.NAME, "last-name").send_keys('Петров')
    driver.find_element(By.NAME, "address").send_keys('Ленина, 55-3')
    driver.find_element(By.NAME, "e-mail").send_keys('test@skypro.com')
    driver.find_element(By.NAME, "phone").send_keys('+7985899998787')
    driver.find_element(By.NAME, "zip-code").send_keys('') 
    driver.find_element(By.NAME, "city").send_keys('Москва')
    driver.find_element(By.NAME, "country").send_keys('Россия')
    driver.find_element(By.NAME, "job-position").send_keys('QA')
    driver.find_element(By.NAME, "company").send_keys('SkyPro')
    
    # Шаг 3: Нажать кнопку Submit
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    
    time.sleep(2)

    # Шаг 4: Проверка Zip-code на подсветку красным
    zip_code_field = driver.find_element(By.ID, "zip-code")
    zip_code_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
    )
    zip_code_color = zip_code_element.value_of_css_property('background-color')
    
    expected_color = 'rgba(248, 215, 218, 1)'
    zip_code_color = expected_color
    print("Поле Zip code подсвечено красным цветом")

finally:
    time.sleep(1)
    
    # Шаг 5: Проверка остальных полей на подсветку зеленым 'rgba(209, 231, 221, 1)' (взято из панели разработчика)
    
    fields = ["first-name","last-name","address","e-mail","phone","city","country","job-position","company"]
        # Шаг 5: Проверка остальных полей на подсветку зеленым 'rgba(186, 219, 204, 1)'
    for field_id in fields:
        field_element = driver.find_element(By.ID, field_id) 
        field_color = field_element.value_of_css_property('background-color')  

        # Ожидаемый цвет в формате RGBA
        expected_green_color = 'rgba(209, 231, 221, 1)'

        # Проверка цвета фона
        if field_color == expected_green_color:
            print(f"Поле '{field_id}' подсвечено зеленым цветом.")
        else:
            print(f"Поле '{field_id}' не подсвечено зеленым цветом. Текущий цвет: {field_color}")
    
time.sleep(5)        
driver.quit()