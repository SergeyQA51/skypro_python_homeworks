from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  

try:
    # Шаг 1: Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Шаг 2: Авторизуемся как стандартный пользователь 
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user") #(данные авторизации были получены с футера сайта)
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Шаг 3: Добавляем товары в корзину
    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    bolt_tshirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    
    backpack.click()
    bolt_tshirt.click()
    onesie.click()

    # Шаг 4: Переходим в корзину
    cart_button = driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()

    # Шаг 5: Нажимаем Checkout
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Шаг 6: Заполняем форму своими данными
    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.ID, "continue")

    first_name_input.send_keys("Сергей")  
    last_name_input.send_keys("Сергеев")  
    postal_code_input.send_keys("123456")  
    continue_button.click()

    # Шаг 8: Читаем итоговую стоимость
    total_price = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))
    ).text

    # Шаг 9: Закрываем браузер
    print(f"Итоговая сумма: {total_price}")
    
    # Шаг 10: Проверяем, что итоговая сумма равна $58.29
    assert total_price == "Total: $58.29", f"Ожидалось 'Total: $58.29', но получено '{total_price}'"
    print("Итоговая сумма соответствует ожидаемому значению '$58.29'.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()
