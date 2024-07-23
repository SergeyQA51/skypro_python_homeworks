from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
   
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[4]"))
    )
    
    third_image = driver.find_element(By.XPATH, "//img[3]")
    src_value = third_image.get_attribute("src")

    
    print("Значение атрибута src у 3-й картинки:", src_value)

finally:

    driver.quit()
