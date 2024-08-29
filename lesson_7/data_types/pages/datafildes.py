import allure  
from selenium.webdriver.common.by import By  
from selenium.webdriver.remote.webdriver import WebDriver  

@allure.feature("Form Fields")  
class DataFild:  
    def __init__(self, browser: WebDriver) -> None:  
        """  
        Инициализация класса DataFild.  

        :param browser: Экземпляр WebDriver для управления браузером.  
        """  
        self.browser = browser  

    @allure.step("Определение локаторов для полей ввода на странице")  
    def find_fields(self) -> None:  
        """  
        Определяет локаторы для полей ввода на странице.  
        
        :return: None  
        """  
        self.class_first_name = (By.ID, "first-name")  
        self.class_last_name = (By.ID, "last-name")  
        self.class_address = (By.ID, "address")  
        self.class_email = (By.ID, "e-mail")  
        self.class_phone = (By.ID, "phone")  
        self.class_zip_code = (By.ID, "zip-code")  
        self.class_city = (By.ID, "city")  
        self.class_country = (By.ID, "country")  
        self.class_job_position = (By.ID, "job-position")  
        self.class_company = (By.ID, "company")  

    @allure.step("Получение значения атрибута 'class' для поля 'first-name'")  
    def get_class_first_name(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'first-name'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_first_name).get_attribute("class")  

    @allure.step("Получение значения атрибута 'class' для поля 'last-name'")  
    def get_class_last_name(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'last-name'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_last_name).get_attribute("class")  
    
    @allure.step("Получение значения атрибута 'class' для поля 'address'")  
    def get_class_address(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'address'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_address).get_attribute("class")  

    @allure.step("Получение значения атрибута 'class' для поля 'e-mail'")  
    def get_class_email(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'e-mail'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_email).get_attribute("class")  

    @allure.step("Получение значения атрибута 'class' для поля 'phone'")  
    def get_class_phone(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'phone'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_phone).get_attribute("class")  

    @allure.step("Получение значения атрибута 'class' для поля 'zip-code'")  
    def get_class_zip_code(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'zip-code'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_zip_code).get_attribute("class")  

    @allure.step("Получение значения атрибута 'class' для поля 'city'")  
    def get_class_city(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'city'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_city).get_attribute("class")  

    @allure.step("Получение значения атрибута 'class' для поля 'country'")  
    def get_class_country(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'country'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_country).get_attribute("class")  

    @allure.step("Получение значения атрибута 'class' для поля 'job-position'")  
    def get_class_job_position(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'job-position'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_job_position).get_attribute("class")   

    @allure.step("Получение значения атрибута 'class' для поля 'company'")  
    def get_class_company(self) -> str:  
        """  
        Возвращает значение атрибута 'class' для поля 'company'.  

        :return: Значение атрибута 'class' (str).  
        """  
        return self.browser.find_element(*self.class_company).get_attribute("class")  