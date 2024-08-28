from empl_api import ApiEmployee
from company import Company
from empl_db import DbEmployee

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
      "isActive": "true"
  }


def test_get_list_employee2():
    api_result = api.get_list_employee2(param_id)
    api_result = api_result.json()
    db_result = db.get_list_employee(company_id)
    assert len(api_result) == len(db_result)


def test_add_employee2():
    db_result = db.get_list_employee(company_id)
    api.add_new_employee2(body)
    api_response = api.get_list_employee2(param_id)
    api_response = api_response.json()
    assert len(api_response)-len(db_result) == 1


def test_get_new_employee2():
    resp = api.get_list_employee2(param_id)
    api_new_employee = resp.json()[-1]['id']
    db_new_employee = db.get_id_new_employee()
    assert api_new_employee == db_new_employee


def test_create_employee2():  
    db_result = db.get_list_employee(company_id)  
    db.add_new_employee("Sergey", "Sergeev", "88005553535", True, company_id)  
    new_employee_id = db.get_id_new_employee() 

    data_employee = api.get_new_employee2(new_employee_id)  
    data_employee = data_employee.json()  
    print(data_employee)  
    assert data_employee["firstName"] == "Sergey"


def test_edit_employee():  
    db.add_new_employee("Sergey", "Sergeev", "88005553535", True, company_id)  
    id = db.get_id_new_employee()  
    db.edit_employee("Igor", "Nickolaev", "123456768", True, company_id, id)  
    data_employee = api.get_new_employee2(id)  
    data_employee = data_employee.json()     