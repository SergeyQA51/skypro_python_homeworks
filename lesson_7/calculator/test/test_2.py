import allure  
from lesson_10.lesson_7.calculator.pages.calcMainPage import CalcMain  

@allure.feature("Calculator")  
@allure.title("Тестирование калькулятора")  
@allure.description("Проверка правильности работы калькулятора при выполнении операции 7 + 8")  
@allure.severity(allure.severity_level.CRITICAL)  
def test_calculator_assert(chrome_browser):  
    """Тест для проверки работы калькулятора.  
    
    :param chrome_browser: Объект WebDriver для управления браузером.  
    """  
    calcmain = CalcMain(chrome_browser)  
    
    with allure.step("Ввод времени задержки"):  
        calcmain.insert_time()  
    
    with allure.step("Выполнение операции 7 + 8"):  
        calcmain.clicking_button()  
    
    with allure.step("Ожидание получения результата"):  
        result = calcmain.wait_button_gettext()  
    
    with allure.step("Проверка результата на экране"):  
        assert "15" in result, f"Ожидалось, что '15' будет в результате, но получено: '{result}'"