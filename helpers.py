import allure
from faker import Faker


@allure.step('Генерируем данные для регистрации пользователя.')
def generate_data_for_registration():
    fake = Faker(locale="ru_RU")
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return email, password, name


class Constants:
    EMAIL = 'ruzin_8@gmail.com'
    PASSWORD = 'P@ssw0rd'
