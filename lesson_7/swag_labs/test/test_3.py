import allure  
from lesson_10.lesson_7.swag_labs.pages.shopmain import ShopmainPage  
from lesson_10.lesson_7.swag_labs.pages.shopcontainer import ShopContainer  

@allure.feature("Shopping Process Test")  
@allure.title("Тест процесса покупки в интернет-магазине")  
@allure.description("Данный тест проверяет правильность процесса покупки в интернет-магазине, включая регистрацию, добавление товаров и проверку итоговой цены.")  
@allure.severity(allure.severity_level.NORMAL)  
def test_shop(chrome_browser) -> None:  
    """  
    Тестовый сценарий для проверки процесса покупки в интернет-магазине.  

    :param chrome_browser: Экземпляр WebDriver, использующий браузер Chrome (WebDriver).  
    :return: None  
    """  
    expected_total = "58.29"  

    # Инициализация главной страницы магазина  
    with allure.step("Инициализация главной страницы магазина"):  
        shopmain = ShopmainPage(chrome_browser)  
        shopmain.registration_fields()  
        shopmain.buy_issue()  
        shopmain.click_issue()  
        shopmain.into_container()  

    # Инициализация контейнера с корзиной  
    with allure.step("Инициализация контейнера с корзиной"):  
        container = ShopContainer(chrome_browser)  
        container.checkout()  
        container.into()  
    
    # Получение и проверка итоговой цены  
    with allure.step("Получение итоговой цены"):  
        actual_total = container.price()  
        print(f"Итоговая сумма равна ${actual_total}")  
        
    with allure.step("Проверка соответствия итоговой цены ожидаемой"):  
        assert expected_total in actual_total, f"Ожидалась итоговая сумма ${expected_total}, но получена ${actual_total}."
    