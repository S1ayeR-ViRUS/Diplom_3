import allure
from locators.locators_account_profile_page import LocatorsAccountProfilePage
from pages.base_page import BasePage


class AccountProfilePage(BasePage):
    @allure.step('Находим заголовок "Профиль" на странице личного кабинета')
    def show_header_profile_in_account_profile_page(self):
        return self.find_and_wait_element(LocatorsAccountProfilePage.HEADER_PROFILE)

    @allure.step('Переходим в историю заказов, кликнув на кнопку "История заказов"')
    def go_to_order_history_page(self):
        self.click_element_with_wait(LocatorsAccountProfilePage.BUTTON_ORDER_HISTORY)

    @allure.step('Выходим из учетной записи, кликнув на кнопку "Выход"')
    def logout(self):
        self.click_element_with_wait(LocatorsAccountProfilePage.BUTTON_LOGOUT)

    @allure.step('Берем номер заказа из верхнего заказа в истории заказов')
    def get_number_order_from_order_in_history_page(self):
        return self.find_and_wait_element(LocatorsAccountProfilePage.NUMBER_ORDER_HISTORY).text
