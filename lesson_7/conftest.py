import pytest  
import allure  
from selenium import webdriver  


@allure.feature("Browser Setup")  
@allure.title("Фикстура для настройки веб-драйвера Chrome")  
@allure.description("Создает экземпляр WebDriver для браузера Chrome, максимизирует его и закрывает после завершения теста.")  
@allure.severity(allure.severity_level.NORMAL)  
@pytest.fixture()  
def chrome_browser():  
    """  
    Фикстура для настройки и получения экземпляра веб-драйвера Chrome.  

    Эта фикстура создает экземпляр WebDriver для браузера Chrome, открывает его в   
    полноэкранном режиме и возвращает для использования в тестах. После завершения   
    теста браузер закрывается.  

    :return: Экземпляр WebDriver, использующий браузер Chrome (WebDriver).  
    """  
    with allure.step("Инициализация WebDriver для Chrome"):  
        driver = webdriver.Chrome()    # Инициализация WebDriver для Chrome  
        
    with allure.step("Максимизация окна браузера"):  
        driver.maximize_window()        # Максимизация окна браузера  
    
    yield driver                     # Возврат экземпляра WebDriver для использования в тестах  

    with allure.step("Закрытие браузера после завершения теста"):  
        driver.quit()                   # Закрытие браузера после завершения теста

   

