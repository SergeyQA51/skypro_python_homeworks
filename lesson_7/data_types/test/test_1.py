import allure  
from lesson_10.lesson_7.data_types.pages.mainpage import MainPage  
from lesson_10.lesson_7.data_types.pages.datafildes import DataFild  
from selenium.webdriver.remote.webdriver import WebDriver  

@allure.feature("Form Submission Test")  
@allure.title("Тестирование заполнения формы и проверки классов")  
@allure.description("Проверяет, что поля заполнены правильно после нажатия на кнопку отправки.")  
@allure.severity(allure.severity_level.CRITICAL)  
def test_assertion(chrome_browser: WebDriver) -> None:  
    """  
    Выполняет тестовое нажатие на кнопку отправки и проверяет классы элементов,  
    чтобы убедиться, что поля заполнены правильно.  

    :param chrome_browser: Экземпляр WebDriver для работы с браузером (WebDriver).  
    :return: None  
    """  
    main_page = MainPage(chrome_browser)  

    with allure.step("Находим поля на главной странице"):  
        main_page.find_fields()  

    with allure.step("Заполняем поля ввода"):  
        main_page.filling_in_fields()  

    with allure.step("Нажимаем на кнопку отправки"):  
        main_page.click_submit_button()  

    data_fild = DataFild(chrome_browser)  
    data_fild.find_fields()  

    with allure.step("Получаем классы полей"):  
        first_name_class = data_fild.get_class_first_name()  
        last_name_class = data_fild.get_class_last_name()  
        address_class = data_fild.get_class_address()  
        phone_class = data_fild.get_class_phone()  
        city_class = data_fild.get_class_city()  
        country_class = data_fild.get_class_country()  
        job_position_class = data_fild.get_class_job_position()  
        company_class = data_fild.get_class_company()  
        zip_code_class = data_fild.get_class_zip_code()  

    with allure.step("Проверка классов полей"):  
        # Проверяем ОР  
        assert "success" in first_name_class, f"Ожидался класс 'success', но получен: {first_name_class}"  
        assert "success" in last_name_class, f"Ожидался класс 'success', но получен: {last_name_class}"  
        assert "success" in address_class, f"Ожидался класс 'success', но получен: {address_class}"  
        assert "success" in phone_class, f"Ожидался класс 'success', но получен: {phone_class}"  
        assert "success" in city_class, f"Ожидался класс 'success', но получен: {city_class}"  
        assert "success" in country_class, f"Ожидался класс 'success', но получен: {country_class}"  
        assert "success" in job_position_class, f"Ожидался класс 'success', но получен: {job_position_class}"  
        assert "success" in company_class, f"Ожидался класс 'success', но получен: {company_class}"  
        assert "danger" in zip_code_class, f"Ожидался класс 'danger', но получен: {zip_code_class}"
    