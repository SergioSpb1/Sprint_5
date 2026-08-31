from data import Data
from locators import Locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class TestConstructorBlocksNavigation:
    def test_buns_navigate (self, driver, login_valid_user):
        # Убеждаемся, что залогинились
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
        # Уходим на соусы
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES_BUTTON)).click()
        # Возвращаемся на булки
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS_BUTTON)).click()
        # Проверяем, что вкладка Булки - активная 
        assert "tab_tab_type_current" in driver.find_element(*Locators.CONSTRUCTOR_BUNS_BUTTON).get_attribute("class")

    def test_sauces_navigate (self, driver, login_valid_user):
        # Убеждаемся, что залогинились
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
        # Переходим на соусы
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES_BUTTON)).click()
        # Проверяем, что вкладка Соусы - активная 
        assert "tab_tab_type_current" in driver.find_element(*Locators.CONSTRUCTOR_SAUCES_BUTTON).get_attribute("class")

    def test_ingredients_navigate (self, driver, login_valid_user):
        # Убеждаемся, что залогинились
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAIN_ORDER_BUTTON))
        # Переходим на начинки
        WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_INGR_BUTTON)).click()
        # Проверяем, что вкладка Начинки - активная 
        assert "tab_tab_type_current" in driver.find_element(*Locators.CONSTRUCTOR_INGR_BUTTON).get_attribute("class")