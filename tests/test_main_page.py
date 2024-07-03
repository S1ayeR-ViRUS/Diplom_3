import allure
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage


class TestMainPage:
    @allure.title('Проверка, что по клику на "Конструктор" отображается форма контсруктора')
    def test_constructor_visibility(self, driver):
        main_page = MainPage(driver)
        assert main_page.show_constructor_form() == 'Соберите бургер'

    @allure.title('Проверка, что по клику на "Лента заказов" отображается лента заказов.')
    def test_orders_list_visibility(self, driver):
        main_page = MainPage(driver)
        order_page = OrderListPage(driver)
        main_page.go_to_orders_list()
        assert order_page.show_orders_list_form() == 'Лента заказов'

    @allure.title('Проверка, что по клику на ингридиент, появляется всплывающее окно с деталями.')
    def test_ingredient_modal_window_is_open(self, driver):
        main_page = MainPage(driver)
        assert main_page.show_modal_ingredient() == 'Детали ингредиента'

    @allure.title('Проверка, что всплывающее окно с деталями закрывается кликом по крестику.')
    def test_ingredient_modal_window_is_closed(self, driver):
        main_page = MainPage(driver)
        main_page.show_modal_ingredient()
        main_page.click_on_button_сross_in_modal_window_ingredient()
        assert main_page.check_modal_window_is_closed()

    @allure.title('Проверка, что при добавлении ингредиента в заказ, счётчик этого ингридиента увеличивается.')
    def test_add_ingredient_in_order_counters_ingredient_is_increasing(self, driver):
        main_page = MainPage(driver)
        ingr_count_before_add = main_page.get_ingredient_count()
        main_page.drag_and_drop_bun_to_the_constructor_burger()
        ingr_count_after_add = main_page.get_ingredient_count()
        assert ingr_count_after_add > ingr_count_before_add

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ.')
    def test_login_users_can_make_an_order(self, login):
        main_page = MainPage(login)
        main_page.make_an_order()
        assert main_page.find_text_in_modal_order() == 'Ваш заказ начали готовить'
