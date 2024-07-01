from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input[@type="text"]')
    PASSWORD_FIELD = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input[@type="password"]')