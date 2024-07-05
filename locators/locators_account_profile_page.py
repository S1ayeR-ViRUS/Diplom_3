from selenium.webdriver.common.by import By


class LocatorsAccountProfilePage:
    HEADER_PROFILE = (By.XPATH, '//a[text() = "Профиль"]')
    BUTTON_ORDER_HISTORY = (By.XPATH, '//a[text() = "История заказов"]')
    BUTTON_LOGOUT = (By.XPATH, '//button[text() = "Выход"]')
    NUMBER_ORDER_HISTORY = (By.XPATH, '//li/a/div/p[@class = "text text_type_digits-default"]')
