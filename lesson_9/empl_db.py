from sqlalchemy import create_engine  
from sqlalchemy.sql import text  
import allure  

@allure.feature("Database Employee Management")  
class DbEmployee:  
    scripts = {  
        "list_employee": text("select * from employee where company_id =:company_id"),  
        "new_employee": text("insert into employee (first_name, last_name, phone, is_active, company_id) values (:first_name, :last_name, :phone, :is_active, :company_id)"),  
        "id_new_employee": text("select id from employee where company_id = (select max(\"company_id\") from employee) and id = (select max(\"id\") from employee)"),  
        "delete": text("delete from employee where id =:new_id"),  
        "edit": text("update employee set first_name =:first_name, last_name =:last_name, phone =:phone, is_active =:is_active where id =:id")  
    }  

    def __init__(self, connection_string: str) -> None:  
        """  
        Инициализация класса DbEmployee.  

        :param connection_string: Строка подключения к базе данных (str).  
        """  
        self.__db = create_engine(connection_string)  

    @allure.step("Получение списка сотрудников по идентификатору компании")  
    def get_list_employee(self, company_id: int) -> list:  
        """  
        Получает список сотрудников по идентификатору компании.  

        :param company_id: Идентификатор компании (int).  
        :return: Список сотрудников (list).  
        """  
        with self.__db.connect() as connection:  
            result = connection.execute(self.scripts['list_employee'], {'company_id': company_id})  
        list_employee = result.fetchall()  # Получаем все записи  
        allure.attach(f'Получен список сотрудников для company_id={company_id}', name='Employee List Retrieval', attachment_type=allure.attachment_type.TEXT)  
        return list_employee  

    @allure.step("Получение идентификатора последнего добавленного сотрудника")  
    def get_id_new_employee(self) -> int:  
        """  
        Получает идентификатор последнего добавленного сотрудника.  

        :return: Идентификатор нового сотрудника (int).  
        """  
        with self.__db.connect() as connection:  
            result = connection.execute(self.scripts['id_new_employee'])  
        new_employee = result.scalar()  # Получает одно значение (ID нового сотрудника)  
        allure.attach(f'Получен идентификатор нового сотрудника: {new_employee}', name='New Employee ID Retrieval', attachment_type=allure.attachment_type.TEXT)  
        return new_employee  

    @allure.step("Добавление нового сотрудника")  
    def add_new_employee(self, first_name: str, last_name: str, phone: str, is_active: bool, company_id: int) -> None:  
        """  
        Добавляет нового сотрудника в базу данных.  

        :param first_name: Имя сотрудника (str).  
        :param last_name: Фамилия сотрудника (str).  
        :param phone: Номер телефона сотрудника (str).  
        :param is_active: Статус активности сотрудника (bool).  
        :param company_id: Идентификатор компании (int).  
        :return: None  
        """  
        with self.__db.connect() as connection:  
            connection.execute(self.scripts['new_employee'], {  
                'first_name': first_name,  
                'last_name': last_name,  
                'phone': phone,  
                'is_active': is_active,  
                'company_id': company_id  
            })  
        allure.attach(f'Добавлен новый сотрудник: {first_name} {last_name}, Phone: {phone}, Active: {is_active}, Company ID: {company_id}', name='Add New Employee', attachment_type=allure.attachment_type.TEXT)  

    @allure.step("Обновление данных о сотруднике")  
    def edit_employee(self, first_name: str, last_name: str, phone: str, is_active: bool, company_id: int, id: int) -> None:  
        """  
        Обновляет данные о сотруднике.  

        :param first_name: Имя сотрудника (str).  
        :param last_name: Фамилия сотрудника (str).  
        :param phone: Номер телефона сотрудника (str).  
        :param is_active: Статус активности сотрудника (bool).  
        :param company_id: Идентификатор компании (int).  
        :param id: Идентификатор сотрудника (int).  
        :return: None  
        """  
        with self.__db.connect() as connection:  
            connection.execute(self.scripts['edit'], {  
                'first_name': first_name,  
                'last_name': last_name,  
                'phone': phone,  
                'is_active': is_active,  
                'company_id': company_id,  
                'id': id  
            })  
        allure.attach(f'Обновлены данные сотрудника ID {id}: {first_name} {last_name}, Phone: {phone}, Active: {is_active}', name='Edit Employee', attachment_type=allure.attachment_type.TEXT)  

    @allure.step("Удаление сотрудника")  
    def delete(self, id: int) -> None:  
        """  
        Удаляет сотрудника по идентификатору.  

        :param id: Идентификатор сотрудника (int).  
        :return: None  
        """  
        with self.__db.connect() as connection:  
            connection.execute(self.scripts['delete'], {'new_id': id})  
        allure.attach(f'Удален сотрудник с ID: {id}', name='Delete Employee', attachment_type=allure.attachment_type.TEXT)