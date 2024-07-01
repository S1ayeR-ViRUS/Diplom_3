import allure
from data import Urls
from helpers import Constants
from locators.locators_forgot_password_page import LocatorsForgotPasswordPage
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Переходим на страницу восставновления пароля по ссылке "Восстановить пароль"')
    def go_to_forgot_password_page(self):
        self.click_element_with_wait(LocatorsForgotPasswordPage.LINK_FORGOT_PASSWORD)

    @allure.step('Ожидаем, пока прогрузится кнопка "Восстановить пароль"')
    def wait_for_load_link_forgot_password(self):
        self.wait_for_load_element(LocatorsForgotPasswordPage.LINK_FORGOT_PASSWORD)

    @allure.step('Открываем страницу восставновления пароля')
    def open_forgot_password_page(self):
        self.open_page(Urls.URL_MAIN_PAGE + Urls.URL_FORGOT_PASSWORD)

    @allure.step('Вводим в поле "Email" почту')
    def set_email(self):
        self.set_value(LocatorsForgotPasswordPage.FIELD_EMAIL, Constants.EMAIL)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def go_to_reset_password_page(self):
        self.click_element_with_wait(LocatorsForgotPasswordPage.BUTTON_RECOVER)

    @allure.step('Ожидаем, пока прогрузится заголовок "Восстановление пароля"')
    def wait_for_load_headers_reset_password(self):
        return self.find_and_wait_element(LocatorsForgotPasswordPage.HEADING_TEXT).text

    @allure.step('Вводим новый пароль')
    def set_new_password(self):
        self.find_and_wait_element(LocatorsForgotPasswordPage.FIELD_PASSWORD)
        self.set_value(LocatorsForgotPasswordPage.FIELD_PASSWORD, Constants.PASSWORD)

    @allure.step('Кликаем на кнопку "показать/скрыть пароль"')
    def click_to_button_visibility(self):
        self.click_element_with_wait(LocatorsForgotPasswordPage.BUTTON_VISIBILITY_PASSWORD)

    @allure.step('Находим подсветку поля "Пароль"')
    def find_element_field_password_active(self):
        return self.find_and_wait_element(LocatorsForgotPasswordPage.FIELD_PASSWORD_ACTIVE)
