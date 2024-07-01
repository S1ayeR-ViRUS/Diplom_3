import allure
from data import Urls
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage


class TestAccountProfilePage:
    @allure.description('Проверка отображения личного кабинета по клику на кнопку "Личный кабинет",'
                        ' когда пользователь авторизован')
    def test_go_to_forgot_password_page_click_on_link_recover_page(self, login):
        account_profile_page = AccountProfilePage(login)
        main_page = MainPage(login)
        main_page.go_to_account_profile()
        assert account_profile_page.show_header_profile_in_account_profile_page().text == 'Профиль'

    @allure.description('Проверка отображения личного кабинета по клику на кнопку "Личный кабинет",'
                        ' когда пользователь авторизован')
    def test_go_to_account_profile_when_user_login(self, login):
        account_profile_page = AccountProfilePage(login)
        main_page = MainPage(login)
        main_page.go_to_account_profile()
        account_profile_page.go_to_order_history_page()
        account_profile_page.wait_for_open_page(Urls.URL_MAIN_PAGE + Urls.URL_ORDER_HISTORY)
        assert login.current_url == Urls.URL_MAIN_PAGE + Urls.URL_ORDER_HISTORY

    @allure.description('Проверка выхода из аккаунта по клику на кнопку "Выход"')
    def test_logout_of_profile_by_click_button_logout(self, login):
        account_profile_page = AccountProfilePage(login)
        main_page = MainPage(login)
        main_page.go_to_account_profile()
        account_profile_page.logout()
        account_profile_page.wait_for_open_page(Urls.URL_MAIN_PAGE + Urls.URL_LOGIN_PAGE)
        assert login.current_url == Urls.URL_MAIN_PAGE + Urls.URL_LOGIN_PAGE
