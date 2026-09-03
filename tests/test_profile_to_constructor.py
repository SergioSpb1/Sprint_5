from data import Data
from locators import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestProfile:
    def test_constructor_button (self, driver, login_valid_user):
        # убеждаемся, что пользователь успешно залогинен 
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
        #Переходим в ЛК
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.MAIN_PROFILE_BUTTON)).click()
        #Кликаем кнопку "Конструктор"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_CONSTRUCTOR_BUTTON)).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_COMBINE_TEXT))

    def test_logo_click (self, driver, login_valid_user):
        # убеждаемся, что пользователь успешно залогинен 
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.MAIN_PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_LOGO)).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_COMBINE_TEXT))
