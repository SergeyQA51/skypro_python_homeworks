import allure  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.common.by import By  
from lesson_10.lesson_7.constants import Calculator_URL  
from selenium.webdriver.remote.webdriver import WebDriver  


@allure.feature("Calculator")  
class CalcMain:  
    def __init__(self, browser: WebDriver) -> None:  
        """  
        Инициализация класса CalcMain.  

        :param browser: Экземпляр WebDriver для управления браузером.  
        """  
        self.browser = browser  
        self.browser.get(Calculator_URL)  

    @allure.step("Ввод значения задержки в поле ввода")  
    def insert_time(self) -> None:  
        """  
        Вводит значение задержки в поле ввода.  

        :return: None  
        """  
        delay_input = self.browser.find_element(By.ID, "delay")  
        delay_input.clear()  
        delay_input.send_keys(45)  

    @allure.step("Нажатие кнопок на калькуляторе для выполнения операции 7 + 8")  
    def clicking_button(self) -> None:  
        """  
        Нажимает кнопки на калькуляторе для выполнения операции 7 + 8.  

        :return: None  
        """  
        self.browser.find_element(By.XPATH, "//span[text() = '7']").click()  
        self.browser.find_element(By.XPATH, "//span[text() = '+']").click()  
        self.browser.find_element(By.XPATH, "//span[text() = '8']").click()  
        self.browser.find_element(By.XPATH, "//span[text() = '='").click()  

    @allure.step("Ожидание изменения текста на экране калькулятора")  
    def wait_button_gettext(self) -> str:  
        """  
        Ожидает, пока текст на экране калькулятора изменится на '15',   
        и возвращает текст с экрана.  

        :return: Текст с экрана калькулятора (str).  
        """  
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))  
        return self.browser.find_element(By.CLASS_NAME, "screen").text  


@allure.title("Тестирование калькулятора")  
@allure.description("Проверка правильности работы калькулятора при выполнении операции 7 + 8")  
@allure.severity(allure.severity_level.CRITICAL)  
def test_calculator(browser: WebDriver):  
    calc = CalcMain(browser)  
    with allure.step("Ввод времени задержки"):  
        calc.insert_time()  
    with allure.step("Выполнение операции 7 + 8"):  
        calc.clicking_button()  
    result = calc.wait_button_gettext()  
    with allure.step("Проверка результата"):  
        assert result == "15", f"Ожидалось '15', но получено '{result}'"
                                              