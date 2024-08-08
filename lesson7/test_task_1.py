import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "e-mail").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone)
        self.driver.find_element(By.NAME, "zip-code").send_keys(zip_code)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "country").send_keys(country)
        self.driver.find_element(By.NAME, "job-position").send_keys(job_position)
        self.driver.find_element(By.NAME, "company").send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    def check_zip_code_color(self):
        zip_code_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
        )
        zip_code_color = zip_code_element.value_of_css_property('background-color')
        return zip_code_color

    def check_other_fields_color(self, field_ids):
        expected_color = 'rgba(209, 231, 221, 1)'
        field_colors = {}
        
        for field_id in field_ids:
            field_element = self.driver.find_element(By.ID, field_id)
            field_color = field_element.value_of_css_property('background-color')
            field_colors[field_id] = field_color

        return field_colors


@pytest.fixture
def driver():
    service = Service('C:/webdrivers/chromedriver.exe') 
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



def test_form_submission(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    form_page = FormPage(driver)

    # Заполнение формы
    form_page.fill_form('Иван', 'Петров', 'Ленина, 55-3', 'test@skypro.com', '+7985899998787', '', 'Москва', 'Россия', 'QA', 'SkyPro')
    form_page.submit_form()

    # Проверка цвета для поля ZIP
    zip_code_color = form_page.check_zip_code_color()
    expected_zip_color = 'rgba(248, 215, 218, 1)'
    assert zip_code_color == expected_zip_color, f'Цвет поля Zip code должен быть {expected_zip_color}, но найден {zip_code_color}'
    print("Поле 'zip-code' подсвечено красным цветом.")

    # Проверка других полей
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    field_colors = form_page.check_other_fields_color(fields)
    for field_id in fields:
        assert field_colors[field_id] == 'rgba(209, 231, 221, 1)', f'Цвет поля {field_id} должен быть rgba(209, 231, 221, 1)'
        print(f"Поле '{field_id}' подсвечено зеленым цветом.")