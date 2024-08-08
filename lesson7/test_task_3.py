import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Класс страницы для входа
class SauceDemoLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()


# Класс страницы для продуктов
class SauceDemoProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self):
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for item in items_to_add:
            self.driver.find_element(By.ID, item).click()

    def go_to_cart(self):
        cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        cart_button.click()


# Класс страницы для оформления заказа
class SauceDemoCheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self, first_name, last_name, postal_code):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        
        first_name_input = self.driver.find_element(By.ID, "first-name")
        last_name_input = self.driver.find_element(By.ID, "last-name")
        postal_code_input = self.driver.find_element(By.ID, "postal-code")
        continue_button = self.driver.find_element(By.ID, "continue")

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)
        continue_button.click()

    def verify_total_price(self, expected_price):
        total_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))
        ).text
        return total_price


# Тестовый класс для Sauce Demo
class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        print("Настройка драйвера...")  # Отладочное сообщение
        self.driver = webdriver.Chrome()
        yield
        print("Закрытие драйвера...")  # Отладочное сообщение
        self.driver.quit()

    def test_sauce_demo(self):
        self.driver.get("https://www.saucedemo.com/")

        login_page = SauceDemoLoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        products_page = SauceDemoProductsPage(self.driver)
        products_page.add_items_to_cart()
        products_page.go_to_cart()

        checkout_page = SauceDemoCheckoutPage(self.driver)
        checkout_page.checkout("Сергей", "Сергеев", "123456")

        total_price = checkout_page.verify_total_price("Total: $58.29")
        assert total_price == "Total: $58.29", f"Ожидалось 'Total: $58.29', но получено '{total_price}'"

