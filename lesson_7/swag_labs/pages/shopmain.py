import allure  
from selenium.webdriver.common.by import By  
from lesson_10.lesson_7.constants import Shop_URL  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

@allure.feature("Shop Main Page Functionality")  
class ShopmainPage:  
    def __init__(self, browser) -> None:  
        """  
        Инициализация класса ShopmainPage.  

        :param browser: Экземпляр WebDriver для работы с браузером.  
        """  
        self.browser = browser  
        self.browser.get(Shop_URL)  

    @allure.step("Заполнение полей для регистрации и логин")  
    def registration_fields(self) -> None:  
        """  
        Заполняет поля для регистрации (имя пользователя и пароль)   
        и нажимает кнопку логина, ожидая загрузку страницы.  

        :return: None  
        """  
        self._name = (By.ID, "user-name")  
        self._pass = (By.ID, "password")  
        self._log_button = (By.ID, "login-button")  
        
        with allure.step("Ввод имени пользователя"):  
            self.browser.find_element(*self._name).send_keys("standard_user")  
        
        with allure.step("Ввод пароля"):  
            self.browser.find_element(*self._pass).send_keys("secret_sauce")  
        
        with allure.step("Нажатие на кнопку логина"):  
            self.browser.find_element(*self._log_button).click()  
        
        WebDriverWait(self.browser, 5).until(  
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))  
        )  

    @allure.step("Определение элементов товара для добавления в корзину")  
    def buy_issue(self) -> None:  
        """  
        Определяет элементы товара, которые будут добавлены в корзину.  

        :return: None  
        """  
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")   
        self.Sauce_Labs_Bolt_Tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")  
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")  

    @allure.step("Добавление товаров в корзину")  
    def click_issue(self) -> None:  
        """  
        Кликает на товары для добавления их в корзину.  

        :return: None  
        """  
        with allure.step("Добавление рюкзака Sauce Labs в корзину"):  
            self.browser.find_element(*self.Sauce_Labs_Backpack).click()  
        
        with allure.step("Добавление футболки Bolt в корзину"):  
            self.browser.find_element(*self.Sauce_Labs_Bolt_Tshirt).click()  
        
        with allure.step("Добавление комбинезона Sauce Labs в корзину"):  
            self.browser.find_element(*self.Sauce_Labs_Onesie).click()  

    @allure.step("Переход в контейнер с корзиной")  
    def into_container(self) -> None:  
        """  
        Переходит в контейнер с корзиной.  

        :return: None  
        """  
        self.Container = (By.ID, "shopping_cart_container")  
        self.browser.find_element(*self.Container).click()
 