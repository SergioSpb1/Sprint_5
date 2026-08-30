import random
class generator:
    def generate_email():
        name = 'Sergey'
        family_name = 'Averkiev'
        cohort = '53'
        # имя_фамилия_номер когорты_любые 3 цифры@домен 
        random_digits = str(random.randint(100, 999))
        return f"{name}{family_name}_{cohort}_{random_digits}@yandex.ru"

    def generate_valid_password():
        random_code = str(random.randint(1000, 9999))
        return f"pwd{random_code}"

    def generate_invalid_password():
        random_code = str(random.randint(10, 99))
        return f"pwd{random_code}"


