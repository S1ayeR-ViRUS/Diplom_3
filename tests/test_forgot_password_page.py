import allure
from data import Urls
from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage


class TestForgotPasswordPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по клику на ссылку "Восстановить пароль"')
    def test_go_to_forgot_password_page_click_on_link_recover_page(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        main_page = MainPage(driver)
        main_page.go_to_account_profile()
        forgot_password_page.go_to_forgot_password_page()
        assert driver.current_url == Urls.URL_MAIN_PAGE + Urls.URL_FORGOT_PASSWORD

    @allure.title('Проверка, что после ввода почты и клика по кнопке "Восстановить" '
                        'происходит переход на форму "Восстановление пароля"')
    def test_put_email_for_recovery(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.set_email()
        forgot_password_page.go_to_reset_password_page()
        element_text = forgot_password_page.wait_for_load_headers_reset_password()

        assert element_text == 'Восстановление пароля'

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"')
    def test_click_on_button_visibility_open_password(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.set_email()
        forgot_password_page.go_to_reset_password_page()
        forgot_password_page.set_new_password()
        forgot_password_page.click_to_button_visibility()
        element = forgot_password_page.find_element_field_password_active()
        assert element.is_displayed()
