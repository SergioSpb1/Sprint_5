from selenium.webdriver.common.by import By

class Locators:
    REG_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") #Страница регистрации, поле ввода имени
    REG_EMAIL_INPUT = (By.XPATH,"//label[text()='Email']/following-sibling::input") #Страница регистрации, поле ввода e-mail
    REG_PWD_INPUT = (By.XPATH,"//input[@type='password']") #Страница регистрации, поле ввода пароля
    REG_REG_BUTTON = (By.XPATH,"//button[text()='Зарегистрироваться']") #Страница регистрации, кнопка "Зарегистрироваться"
    REG_BAD_PWD_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']") #Страница регистрации, сообщение о некорректном пароле
    REG_LOGIN_LINK = (By.XPATH, "//a[@href='/login']") #Страница регистрации, ссылка Войти около "Уже зарегистрированы?"
    
    MAIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт" на главной 
    MAIN_PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка "Личный кабинет" на главной 
    MAIN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") #Кнопка "Оформить заказ" на главной - используется для проверки успешного логина 
    MAIN_COMBINE_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']") #Текстовый заголовок на главной - используется для проверки перехода на конструктор

    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']") #Страница логина, поле ввода е-мейл
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") #Страница логина, поле ввода пароля
    LOGIN_LOGIN_BUTTON = (By.XPATH,"//button[text()='Войти']") #Страница логина, кнопка "Войти"

    RECOVERY_PAGE_LOGIN_LINK = (By.XPATH, "//a[@href='/login']") #Ccылка "Войти" на странице восстановления пароля 

    PROFILE_CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") #Кнопка "Конструктор" в ЛК
    PROFILE_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") #Логотип  Stellar Burgers в ЛК
    PROFILE_LOGOUT_LINK = (By.XPATH, "//button[text()='Выход']") #Кнопка-ссылка "Выход" в ЛК

    CONSTRUCTOR_SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::div") #Кнопка Соусы в Конструкторе
    CONSTRUCTOR_BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::div") #Кнопка Булки в Конструкторе
    CONSTRUCTOR_INGR_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::div") #Кнопка Начинки в Конструкторе

        