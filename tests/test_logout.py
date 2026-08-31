from data import Data
from locators import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class TestLogout:
    def test_profile_logout (self, driver, login_valid_user):
         
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.MAIN_PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_LOGOUT_LINK)).click()

        assert WebDriverWait(driver, 3).until(EC.url_contains(Data.LOGIN_URL))