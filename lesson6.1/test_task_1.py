from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('path/to/chromedriver')
driver = webdriver.Chrome()

def fillForm():
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    
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

def submitForm():
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

def checkZipCode():
    zipCodeField = driver.find_element(By.ID, "zip-code")
    
    zipCodeElement = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
    )
    
    zipCodeColor = zipCodeElement.value_of_css_property('background-color')
    expectedColor = 'rgba(248, 215, 218, 1)'

    assert zipCodeColor == expectedColor, f'Цвет поля Zip code должен быть {expectedColor}, но найден {zipCodeColor}'
    print("Поле 'zip-code' подсвечено красным цветом.")

def checkOtherFields():
    fields = [
        "first-name", "last-name", "address", 
        "e-mail", "phone", "city", 
        "country", "job-position", "company"
    ]
    expectedGreenColor = 'rgba(209, 231, 221, 1)'

    for fieldId in fields:
        fieldElement = driver.find_element(By.ID, fieldId)
        fieldColor = fieldElement.value_of_css_property('background-color')
        
        assert fieldColor == expectedGreenColor, f'Цвет поля {fieldId} должен быть {expectedGreenColor}, но найден {fieldColor}'
        print(f"Поле '{fieldId}' подсвечено зеленым цветом.")

try:
    fillForm()
    submitForm()
    checkZipCode()
    checkOtherFields()
finally:
    driver.quit()