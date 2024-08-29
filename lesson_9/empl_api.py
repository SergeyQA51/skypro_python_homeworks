import requests  
import allure  

@allure.feature("API Employee Management")  
class ApiEmployee:  
    def __init__(self, url: str) -> None:  
        """  
        Инициализация класса ApiEmployee.  

        :param url: Базовый URL для API (str).  
        """  
        self.url = url  

    @allure.step("Аутентификация пользователя")  
    def auth2(self, login: str = "leonardo", password: str = "leads") -> str:  
        """  
        Выполняет аутентификацию пользователя и возвращает токен.  

        :param login: Логин для аутентификации (str), по умолчанию 'leonardo'.  
        :param password: Пароль для аутентификации (str), по умолчанию 'leads'.  
        :return: Токен пользователя (str).  
        """  
        body = {  
            "username": login,  
            "password": password  
        }  
        response = requests.post(self.url + '/auth/login', json=body)  
        allure.attach(str(body), name='Auth Request Body', attachment_type=allure.attachment_type.JSON)  
        return response.json()["userToken"]  

    @allure.step("Получение списка сотрудников")  
    def get_list_employee2(self, params: dict = None) -> requests.Response:  
        """  
        Получает список сотрудников компании.  

        :param params: Параметры для GET-запроса (dict), по умолчанию None.  
        :return: Ответ API (requests.Response).  
        """  
        response = requests.get(self.url + '/employee', params=params)  
        allure.attach(f'GET {self.url}/employee', name='Request URL', attachment_type=allure.attachment_type.TEXT)  
        allure.attach(str(params), name='Request Params', attachment_type=allure.attachment_type.JSON)  
        return response  

    @allure.step("Добавление нового сотрудника")  
    def add_new_employee2(self, body: dict) -> requests.Response:  
        """  
        Добавляет нового сотрудника.  

        :param body: Данные о новом сотруднике (dict).  
        :return: Ответ API (requests.Response).  
        """  
        headers = {'x-client-token': self.auth2()}  
        response = requests.post(self.url + '/employee/', headers=headers, json=body)  
        allure.attach(str(body), name='New Employee Data', attachment_type=allure.attachment_type.JSON)  
        return response  

    @allure.step("Получение данных сотрудника по ID")  
    def get_new_employee2(self, id: int) -> requests.Response:  
        """  
        Получает данные о сотруднике по заданному идентификатору.  

        :param id: Идентификатор сотрудника (int).  
        :return: Ответ API (requests.Response).  
        """  
        response = requests.get(self.url + '/employee/' + str(id))  
        allure.attach(f'GET {self.url}/employee/{id}', name='Request URL', attachment_type=allure.attachment_type.TEXT)  
        return response  

    @allure.step("Изменение данных о новом сотруднике")  
    def change_new_employee2(self, id: int, new_body: dict) -> requests.Response:  
        """  
        Изменяет данные о сотруднике.  

        :param id: Идентификатор сотрудника (int).  
        :param new_body: Новые данные о сотруднике (dict).  
        :return: Ответ API (requests.Response).  
        """  
        headers = {'x-client-token': self.auth2()}  
        response = requests.patch(self.url + '/employee/' + str(id), headers=headers, json=new_body)  
        allure.attach(str(new_body), name='Updated Employee Data', attachment_type=allure.attachment_type.JSON)  
        return response 