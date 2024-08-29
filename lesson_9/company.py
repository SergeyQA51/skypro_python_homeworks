import allure  
import requests  

@allure.feature("Company Management API")  
class Company:  
    def __init__(self, url: str) -> None:  
        """  
        Инициализация класса Company.  

        :param url: Базовый URL для API (str).  
        """  
        self.url = url  

    @allure.step("Получение идентификатора последней компании")  
    def get_id_company(self) -> int:  
        """  
        Получает идентификатор последней компании.  

        Выполняет GET-запрос к конечной точке '/company' и возвращает   
        идентификатор последней компании из ответа.  

        :return: Идентификатор компании (int).  
        """  
        with allure.step("Выполнение GET-запроса к '/company'"):  
            response = requests.get(self.url + '/company')  
            response.raise_for_status()   
            company_id = response.json()[-1]['id']  
            allure.attach(f'Идентификатор компании: {company_id}', name='Company ID', attachment_type=allure.attachment_type.TEXT)  
            return company_id  

    @allure.step("Создание новой компании")  
    def create_company(self, company_data: dict) -> dict:    
        """  
        Создает новую компанию.  

        Выполняет POST-запрос к конечной точке '/company' с данными   
        о компании в формате JSON и возвращает ответ API.  

        :param company_data: Данные о компании для создания (dict).  
        :return: Ответ API в формате JSON (dict).  
        """  
        with allure.step("Выполнение POST-запроса к '/company'"):  
            response = requests.post(self.url + '/company', json=company_data)  
            response.raise_for_status()  
            allure.attach(str(company_data), name='Company Data Sent', attachment_type=allure.attachment_type.TEXT)  
            return response.json()    

    @allure.step("Удаление компании по идентификатору")  
    def delete_company(self, company_id: int) -> dict:  
        """  
        Удаляет компанию по заданному идентификатору.  

        Выполняет DELETE-запрос к конечной точке '/company/{company_id}'   
        и возвращает ответ API.  

        :param company_id: Идентификатор компании для удаления (int).  
        :return: Ответ API в формате JSON (dict).  
        """  
        with allure.step(f"Выполнение DELETE-запроса к '/company/{company_id}'"):  
            response = requests.delete(self.url + f'/company/{company_id}')  
            response.raise_for_status()   
            return response.json()
