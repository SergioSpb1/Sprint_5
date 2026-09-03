from data import Data
from locators import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestProfile:
    def test_profile_button_click_logined(self, driver, login_valid_user):
        # убеждаемся, что пользователь успешно залогинен 
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PROFILE_BUTTON)).click()

        assert WebDriverWait(driver, 3).until(EC.url_contains(Data.PROFILE_URL))

