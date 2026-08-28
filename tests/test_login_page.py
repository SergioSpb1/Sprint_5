# tests/test_login.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    # Настройка драйвера (то, что мы делали в терминале много раз)
    service = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=service)
    
    # Неявное ожидание на случай медленного интернета
    _driver.implicitly_wait(5) 
    
    yield _driver
    
    # Закрытие браузера после каждого теста
    _driver.quit()


def test_open_main_page(driver):
    """
    Цель: Проверить, что главная страница загружается и содержит заголовок.
    Это наш "дымовой" (smoke) тест.
    """
    # 1. Действие: открыть URL
    driver.get("https://stellarburgers.education-services.ru/")
    
    # 2. Проверка (Assert): убедиться, что мы там, где хотели
    assert "Stellar Burgers" in driver.title