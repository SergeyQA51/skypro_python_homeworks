import allure  
from selenium.webdriver.remote.webdriver import WebDriver  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.common.by import By  
from lesson_10.lesson_7.constants import Test_form_URL  
from lesson_10.lesson_7.data_types.data import *  

@allure.feature("Main Page Form")  
class MainPage:  
    def __init__(self, browser: WebDriver) -> None:  
        """  
        Инициализация класса MainPage.  

        :param browser: Экземпляр WebDriver для управления браузером.  
        """  
        self.browser = browser  
        self.browser.get(Test_form_URL)  

    @allure.step("Определение локаторов для полей ввода и кнопки на странице")  
    def find_fields(self) -> None:  
        """  
        Определяет локаторы для полей ввода и кнопки на странице.  
        
        :return: None  
        """  
        self._first_name = (By.NAME, "first-name")  
        self._last_name = (By.NAME, "last-name")  
        self._address = (By.NAME, "address")  
        self._email = (By.NAME, "e-mail")  
        self._phone = (By.NAME, "phone")  
        self._zip_code = (By.NAME, "zip-code")  
        self._city = (By.NAME, "city")  
        self._country = (By.NAME, "country")  
        self._job_position = (By.NAME, "job-position")  
        self._company = (By.NAME, "company")  
        self._button = (By.TAG_NAME, "button")  

    @allure.step("Заполнение полей ввода данными")  
    def filling_in_fields(self) -> None:  
        """  
        Заполняет поля ввода данными.  

        :return: None  
        """  
        self.browser.find_element(*self._first_name).send_keys(first_name)  
        self.browser.find_element(*self._last_name).send_keys(last_name)  
        self.browser.find_element(*self._address).send_keys(address)  
        self.browser.find_element(*self._email).send_keys(email)  
        self.browser.find_element(*self._phone).send_keys(phone)  
        self.browser.find_element(*self._zip_code).send_keys(zip_code)  
        self.browser.find_element(*self._city).send_keys(city)  
        self.browser.find_element(*self._country).send_keys(country)  
        self.browser.find_element(*self._job_position).send_keys(job_position)  
        self.browser.find_element(*self._company).send_keys(company)  

    @allure.step("Ожидание пока кнопка станет кликабельной и нажатие на нее")  
    def click_submit_button(self) -> None:  
        """  
        Ожидает, пока кнопка становится кликабельной, и нажимает на нее.  

        :return: None  
        """  
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()
