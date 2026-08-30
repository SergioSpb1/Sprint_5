from generators import generator
from data import Data
from locators import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time #удалить перед отправкой

class TestBurgers: 
    def test_registration_success(self, driver):

        driver.get(Data.REG_URL)
        name_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_NAME_INPUT))
        name_input.send_keys(Data.NAME)

        email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_EMAIL_INPUT))
        email_input.send_keys(generator.generate_email())

        pwd_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_PWD_INPUT))
        pwd_input.send_keys(generator.generate_valid_password())
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_REG_BUTTON)).click()
        
        assert WebDriverWait(driver,5).until(EC.url_contains(Data.LOGIN_URL))
        

    def test_registration_unsuccess_invalid_password (self, driver):

        driver.get(Data.REG_URL)
        name_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_NAME_INPUT))
        name_input.send_keys(Data.NAME)

        email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_EMAIL_INPUT))
        email_input.send_keys(generator.generate_email())

        pwd_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_PWD_INPUT))
        pwd_input.send_keys(generator.generate_invalid_password())
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_REG_BUTTON)).click()

        assert WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.REG_BAD_PWD_MESSAGE))