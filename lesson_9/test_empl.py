from lesson_10.lesson_9.empl_api import ApiEmployee  
from lesson_10.lesson_9.company import Company  
from lesson_10.lesson_9.empl_db import DbEmployee  
import allure  

db = DbEmployee("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")  
company = Company("https://x-clients-be.onrender.com")  
param_id = "?company=" + str(company.get_id_company())  
company_id = company.get_id_company()  
api = ApiEmployee("https://x-clients-be.onrender.com")  

body = {  
    "id": 1010108711,  
    "firstName": "Sergey",  
    "lastName": "Sergeev",  
    "middleName": 'string',  
    "companyId": company_id,  
    "email": 'mail@mail.ru',  
    "url": "string",  
    "phone": "88005553535",  
    "birthdate": "2023-08-14T11:02:45.622Z",  
    "isActive": True   
}   

@allure.title("Тестирование получения списка сотрудников")  
@allure.description("Сравнивает количество сотрудников из API и базы данных для одной компании.")  
@allure.feature("Employee API")  
@allure.severity(allure.severity_level.NORMAL)  
def test_get_list_employee2() -> None:  
    with allure.step("Получаем список сотрудников из API"):  
        api_result = api.get_list_employee2(param_id)  
        api_result = api_result.json()  

    with allure.step("Получаем список сотрудников из базы данных"):  
        db_result = db.get_list_employee(company_id)  

    with allure.step("Сравниваем количество сотрудников"):  
        assert len(api_result) == len(db_result)  

@allure.title("Тестирование добавления нового сотрудника")  
@allure.description("Сравнивает количество сотрудников до и после добавления нового сотрудника через API.")  
@allure.feature("Employee API")  
@allure.severity(allure.severity_level.CRITICAL)  
def test_add_employee2() -> None:  
    with allure.step("Получаем количество сотрудников до добавления нового"):  
        db_result = db.get_list_employee(company_id)  

    with allure.step("Добавляем нового сотрудника через API"):  
        api.add_new_employee2(body)  

    with allure.step("Получаем список сотрудников из API после добавления"):  
        api_response = api.get_list_employee2(param_id)  
        api_response = api_response.json()  

    with allure.step("Проверяем, что добавился новый сотрудник"):  
        assert len(api_response) - len(db_result) == 1  

@allure.title("Тестирование получения нового сотрудника")  
@allure.description("Проверяет, что идентификатор нового сотрудника из API равен идентификатору, полученному из базы данных.")  
@allure.feature("Employee API")  
@allure.severity(allure.severity_level.NORMAL)  
def test_get_new_employee2() -> None:  
    with allure.step("Получаем список сотрудников из API"):  
        resp = api.get_list_employee2(param_id)  
        api_new_employee = resp.json()[-1]['id']  

    with allure.step("Получаем идентификатор нового сотрудника из базы данных"):  
        db_new_employee = db.get_id_new_employee()  

    with allure.step("Сравниваем идентификаторы сотрудников"):  
        assert api_new_employee == db_new_employee  

@allure.title("Тестирование создания сотрудника через базу данных")  
@allure.description("Добавляет нового сотрудника в базу и проверяет, что он корректно возвращается через API.")  
@allure.feature("Employee API")  
@allure.severity(allure.severity_level.CRITICAL)  
def test_create_employee2() -> None:  
    with allure.step("Получаем количество сотрудников до добавления нового в базу"):  
        db_result = db.get_list_employee(company_id)  

    with allure.step("Добавляем нового сотрудника в базу"):  
        db.add_new_employee("Sergey", "Sergeev", "88005553535", True, company_id)  

    with allure.step("Получаем идентификатор нового сотрудника"):  
        new_employee_id = db.get_id_new_employee()   

    with allure.step("Получаем данные нового сотрудника из API"):  
        data_employee = api.get_new_employee2(new_employee_id)  
        data_employee = data_employee.json()  
        print(data_employee)  

    with allure.step("Проверяем, что имя нового сотрудника соответствует ожидаемому"):  
        assert data_employee["firstName"] == "Sergey"  

@allure.title("Тестирование редактирования данных о сотруднике")  
@allure.description("Добавляет нового сотрудника, затем редактирует его данные и проверяет, что изменения применились.")  
@allure.feature("Employee API")  
@allure.severity(allure.severity_level.NORMAL)  
def test_edit_employee() -> None:  
    with allure.step("Добавляем нового сотрудника"):  
        db.add_new_employee("Sergey", "Sergeev", "88005553535", True, company_id)  

    with allure.step("Получаем идентификатор нового сотрудника"):  
        id = db.get_id_new_employee()  

    with allure.step("Редактируем данные сотрудника"):  
        db.edit_employee("Igor", "Nickolaev", "123456768", True, company_id, id)  

    with allure.step("Получаем обновленные данные сотрудника из API"):  
        data_employee = api.get_new_employee2(id)  
        data_employee = data_employee.json()  
        print(data_employee)     
    
    
         