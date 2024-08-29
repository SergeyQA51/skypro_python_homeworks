import allure  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.support.ui import WebDriverWait  

@allure.feature("Shop Checkout Process")  
class ShopContainer:  
    def __init__(self, browser) -> None:  
        """  
        Инициализация класса ShopContainer.  

        :param browser: Экземпляр WebDriver для работы с браузером.  
        """  
        self.browser = browser  

    @allure.step("Нажатие на кнопку 'checkout'")  
    def checkout(self) -> None:  
        """  
        Нажимает на кнопку 'checkout'.  

        :return: None  
        """  
        self.check = (By.ID, "checkout")  
        self.browser.find_element(*self.check).click()  

    @allure.step("Заполнение формы имени, фамилии и почтового индекса")  
    def into(self) -> None:  
        """  
        Заполняет поля для имени, фамилии и почтового индекса,   
        а затем нажимает на кнопку 'continue'.  

        :return: None  
        """  
        self.first_name = (By.ID, "first-name")  
        self.browser.find_element(*self.first_name).send_keys("Ivan")  
        
        self.last_name = (By.ID, "last-name")  
        self.browser.find_element(*self.last_name).send_keys("Ivanov")  
        
        self.postcode = (By.ID, "postal-code")  
        self.browser.find_element(*self.postcode).send_keys("123456")  
        
        self.continue_button = (By.ID, "continue")  
        self.browser.find_element(*self.continue_button).click()  

    @allure.step("Получение общей стоимости")  
    def price(self) -> str:  
        """  
        Ожидает появления элемента с общей стоимостью и возвращает его значение.  

        :return: Общая стоимость как строка (str).  
        """  
        WebDriverWait(self.browser, 10, 0.1).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))  
        )  
        total_price = self.browser.find_element(By.CSS_SELECTOR, ".summary_total_label")  
        total = total_price.text.strip().replace("Total: $", "")  
        return total