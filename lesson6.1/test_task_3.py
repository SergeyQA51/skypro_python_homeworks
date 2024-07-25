import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        print("Настройка драйвера...")  # Отладочное сообщение
        self.driver = webdriver.Chrome()
        yield
        print("Закрытие драйвера...")  # Отладочное сообщение
        self.driver.quit()

    def open_website(self):
        print("Открытие сайта...")  # Отладочное сообщение
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        print("Вход в систему...")  # Отладочное сообщение
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    def add_items_to_cart(self):
        print("Добавление товаров в корзину...")  # Отладочное сообщение
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for item in items_to_add:
            self.driver.find_element(By.ID, item).click()

    def go_to_cart(self):
        print("Переход в корзину...")  # Отладочное сообщение
        cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        cart_button.click()

    def checkout(self, first_name, last_name, postal_code):
        print("Оформление заказа...")  # Отладочное сообщение
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
        print("Проверка итоговой цены...")  # Отладочное сообщение
        total_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))
        ).text
        assert total_price == expected_price, f"Ожидалось '{expected_price}', но получено '{total_price}'"
        print(f"Итоговая сумма: {total_price}")

    def test_sauce_demo(self):
        self.open_website()
        self.login("standard_user", "secret_sauce")
        self.add_items_to_cart()
        self.go_to_cart()
        self.checkout("Сергей", "Сергеев", "123456")
        self.verify_total_price("Total: $58.29")
