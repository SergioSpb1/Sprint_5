import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from generators import generator
from locators import Locators 
from data import Data


@pytest.fixture(scope="function")
def driver():
    _driver = webdriver.Chrome()

    yield _driver

    _driver.quit()

@pytest.fixture(scope="function")
def create_valid_user(driver):
    email = generator.generate_email()
    pwd = generator.generate_valid_password()

    driver.get(Data.REG_URL)

    name_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_NAME_INPUT))
    name_input.send_keys(Data.NAME)

    email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_EMAIL_INPUT))
    email_input.send_keys(email)

    pwd_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_PWD_INPUT))
    pwd_input.send_keys(pwd)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_REG_BUTTON)).click()

    return {"email": email, "password": pwd}

@pytest.fixture(scope="function")
def login_valid_user(driver, create_valid_user):
    driver.get(Data.LOGIN_URL)

    WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT)).send_keys(create_valid_user["email"])
    WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_INPUT)).send_keys(create_valid_user["password"])
    WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_LOGIN_BUTTON)).click()
