import allure
from locators.locators_main_page import LocatorsMainPage
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открываем страницу личного кабинета.')
    def go_to_account_profile(self):
        self.click_element(LocatorsMainPage.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Ожидаем загрузки главной страницы.')
    def wait_for_load_main_page(self):
        self.find_and_wait_element(LocatorsMainPage.MAIN_PAGE)

    @allure.step('Открываем страницу ленты заказов.')
    def go_to_orders_list(self):
        self.click_element(LocatorsMainPage.BUTTON_ORDER_LIST)

    @allure.step('Кликаем на кнопку "Лента заказов", кликаем на кнопку "Конструктор, '
                 'находим заголовок контсруктора "Соберите заказ"')
    def show_constructor_form(self):
        self.click_element_with_wait(LocatorsMainPage.BUTTON_ORDER_LIST)
        self.click_element_with_wait(LocatorsMainPage.BUTTON_CONSTRUCTOR)
        return self.find_and_wait_element(LocatorsMainPage.HEADER_MAIN_PAGE).text

    @allure.step('Нажимаем на ингредиент и находим заголовок в модальном окне')
    def show_modal_ingredient(self):
        self.click_element_with_wait(LocatorsMainPage.BUN_FIRST_IN_LIST)
        return self.find_and_wait_element(LocatorsMainPage.HEADER_MODAL_INGREDIENT).text

    @allure.step('Нажимаем крестик в модальном окне с деталями ингредиента')
    def click_on_button_сross_in_modal_window_ingredient(self):
        self.click_element_with_wait(LocatorsMainPage.BUTTON_CROSS_IN_MODAL_INGREDIENT)

    @allure.step('Проверяем закрытие модального окна')
    def check_modal_window_is_closed(self):
        return self.check_element_is_invisible(LocatorsMainPage.INGR_MODAL)

    @allure.step('Перетаскиваем булку в конструктор бургера')
    def drag_and_drop_bun_to_the_constructor_burger(self):
        self.drag_and_drop_ingredient(LocatorsMainPage.BUN_FIRST_IN_LIST, LocatorsMainPage.BUN_IN_CONSTRUCTOR)

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_on_button_confirm_order(self):
        self.click_element(LocatorsMainPage.BUTTON_CONFIRM_ORDER)

    @allure.step('Нажимаем крестик в модальном окне сформированного заказа')
    def click_on_button_сross_in_modal_window_order(self):
        self.click_element_with_wait(LocatorsMainPage.BUTTON_CROSS_IN_MODAL)

    @allure.step('Достаем номер заказа')
    def get_number_order(self):
        return self.find_and_wait_element(LocatorsMainPage.ORDER_NUMBER).text

    @allure.step('Делаем заказ')
    def make_an_order(self):
        self.drag_and_drop_bun_to_the_constructor_burger()
        self.click_on_button_confirm_order()
        self.click_on_button_сross_in_modal_window_order()

    @allure.step('Находим текст в модальном окне "Ваш заказ начали готовить"')
    def find_text_in_modal_order(self):
        return self.find_and_wait_element(LocatorsMainPage.TEXT_IN_ORDER_MODAL).text

    @allure.step('Находим номер счетчика ингредиента')
    def get_ingredient_count(self):
        return self.find_and_wait_element(LocatorsMainPage.COUNTER_INGREDIENT).text

    @allure.step('Делаем заказ и вытаскиваем его номер')
    def make_an_order_and_get_number(self):
        self.drag_and_drop_bun_to_the_constructor_burger()
        self.click_on_button_confirm_order()
        self.wait_for_element_to_change_text(LocatorsMainPage.ORDER_NUMBER, '9999')
        number = self.get_number_order()
        self.click_on_button_сross_in_modal_window_order()
        return number
