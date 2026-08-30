from data import Data
from locators import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestLogins:
    def test_account_button_login(self, driver, create_valid_user):

        driver.get(Data.BURGERS_URL)

        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.MAIN_ACCOUNT_BUTTON)).click()

        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT)).send_keys(create_valid_user["email"])
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_INPUT)).send_keys(create_valid_user["password"])
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_LOGIN_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))

    def test_profile_button_login(self, driver, create_valid_user):
    
            driver.get(Data.BURGERS_URL)
    
            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.MAIN_PROFILE_BUTTON)).click()
    
            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT)).send_keys(create_valid_user["email"])
            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_INPUT)).send_keys(create_valid_user["password"])
            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_LOGIN_BUTTON)).click()
    
            assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))

    def test_reg_page_login(self, driver, create_valid_user):
    
            driver.get(Data.REG_URL)

            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.REG_LOGIN_LINK)).click()
    
            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT)).send_keys(create_valid_user["email"])
            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_INPUT)).send_keys(create_valid_user["password"])
            WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_LOGIN_BUTTON)).click()
    
            assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))

    def test_pwdrecovery_page_login(self, driver, create_valid_user):
        
                driver.get(Data.PWD_RECOVERY_URL)
                time.sleep(5)
    
                WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.RECOVERY_PAGE_LOGIN_LINK)).click()
        
                WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT)).send_keys(create_valid_user["email"])
                WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_PASSWORD_INPUT)).send_keys(create_valid_user["password"])
                WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.LOGIN_LOGIN_BUTTON)).click()
        
                assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
