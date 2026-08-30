from selenium.webdriver.common.by import By

class Locators:
    REG_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REG_EMAIL_INPUT = (By.XPATH,"//label[text()='Email']/following-sibling::input")
    REG_PWD_INPUT = (By.XPATH,"//input[@type='password']")
    REG_REG_BUTTON = (By.XPATH,"//button[text()='Зарегистрироваться']")
    REG_BAD_PWD_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    REG_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    
    MAIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    MAIN_PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    MAIN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_LOGIN_BUTTON = (By.XPATH,"//button[text()='Войти']")

    RECOVERY_PAGE_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")