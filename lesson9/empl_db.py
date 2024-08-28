from sqlalchemy import create_engine
from sqlalchemy.sql import text


class DbEmployee:
    scripts = {
        "list_employee": text("select * from employee where company_id =:company_id"),
        "new_employee": text("insert into employee (first_name, last_name, phone, is_active, company_id) values (:first_name, :last_name, :phone, :is_active, :company_id)"),
        "id_new_employee": text("select id from employee where company_id = (select max(\"company_id\") from employee) and id = (select max(\"id\") from employee)"),
        "delete": text("delete from employee where id =:new_id"),
        "edit": text("update employee set first_name =:first_name, last_name =:last_name, phone =:phone, is_active =:is_active where id =:id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)


    def get_list_employee(self, company_id):  
        with self.__db.connect() as connection:  
            result = connection.execute(self.scripts['list_employee'], {'company_id': company_id})  # Обратите внимание на передачу параметров в словаре  
        list_employee = result.fetchall()  # Получаем все записи  
        return list_employee 

    def get_id_new_employee(self):  
        with self.__db.connect() as connection:  
            result = connection.execute(self.scripts['id_new_employee'])  
        new_employee = result.scalar()  # Получить одно значение (ID нового сотрудника)  
        return new_employee

    def add_new_employee(self, first_name, last_name, phone, is_active, company_id):  
        with self.__db.connect() as connection:  
            connection.execute(self.scripts['new_employee'], {'first_name': first_name, 'last_name': last_name, 'phone': phone, 'is_active': is_active, 'company_id': company_id})  

    def edit_employee(self, first_name, last_name, phone, is_active, company_id, id):  
        with self.__db.connect() as connection:  
            connection.execute(self.scripts['edit'], {  
                'first_name': first_name,  
                'last_name': last_name,  
                'phone': phone,  
                'is_active': is_active,  
                'company_id': company_id,  
                'id': id  
        })  

    def delete(self, id):
        self.__db.execute(self.scripts['delete'], new_id =id)