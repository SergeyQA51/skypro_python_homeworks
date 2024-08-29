import requests  

class Company:  
    def __init__(self, url) -> None:  
        self.url = url  

    def get_id_company(self):  
        response = requests.get(self.url + '/company')  
        response.raise_for_status() 
        return response.json()[-1]['id']  

    def create_company(self, company_data):    
        response = requests.post(self.url + '/company', json=company_data)  
        response.raise_for_status()    
        return response.json()    

    def delete_company(self, company_id):  
        response = requests.delete(self.url + f'/company/{company_id}')  
        response.raise_for_status()   
        return response.json() 
