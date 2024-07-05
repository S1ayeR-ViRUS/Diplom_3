from selenium.webdriver.common.by import By


class LocatorsForgotPasswordPage:
    LINK_FORGOT_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')
    FIELD_EMAIL = (By.XPATH, '//input[@name="name"]')
    BUTTON_RECOVER = (By.XPATH, '//button[text() = "Восстановить"]')
    FIELD_PASSWORD = (By.XPATH, './/input[@class = "text input__textfield text_type_main-default" '
                                'and @name = "Введите новый пароль"]')
    BUTTON_VISIBILITY_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    FIELD_PASSWORD_ACTIVE = \
        (By.XPATH, './/div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
    HEADING_TEXT = (By.XPATH, '//h2[text() = "Восстановление пароля"]')
