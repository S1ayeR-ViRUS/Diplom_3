import allure
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage


class TestOrderListPage:
    @allure.title('Проверяем, что по клику на заказ открывается модальное окно с деталями заказа')
    def test_open_modal_window_of_order_by_click_on_first_order_in_list(self, driver):
        order_list_page = OrderListPage(driver)
        order_list_page.open_order_list_page()
        order_list_page.click_in_first_order_in_list()
        assert order_list_page.get_text_from_modal_window() == 'Cостав'

    @allure.title('Проверяем, что заказы пользователя из раздела "История заказов" '
                        'отображаются на странице "Лента заказов"')
    def test_users_order_is_exist_in_order_list(self, login):
        order_list_page = OrderListPage(login)
        main_page = MainPage(login)
        account_profile_page = AccountProfilePage(login)
        main_page.make_an_order()
        main_page.go_to_account_profile()
        account_profile_page.go_to_order_history_page()
        number_order_history = account_profile_page.get_number_order_from_order_in_history_page()
        order_list_page.open_order_list_page()
        order_texts = order_list_page.collect_order_numbers()
        assert number_order_history in order_texts

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_counter_all_orders_increases_after_new_order(self, login):
        order_list_page = OrderListPage(login)
        main_page = MainPage(login)
        main_page.go_to_orders_list()
        all_time_count_before = order_list_page.show_all_time_done_orders()
        order_list_page.go_to_main_page()
        main_page.make_an_order()
        order_list_page.open_order_list_page()
        all_time_count_after = order_list_page.show_all_time_done_orders()
        assert all_time_count_after > all_time_count_before

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_counter_today_orders_increases_after_new_order(self, login):
        order_list_page = OrderListPage(login)
        main_page = MainPage(login)
        main_page.go_to_orders_list()
        today_time_count_before = order_list_page.show_today_done_orders()
        order_list_page.go_to_main_page()
        main_page.make_an_order()
        order_list_page.open_order_list_page()
        today_time_count_after = order_list_page.show_today_done_orders()
        assert today_time_count_after > today_time_count_before

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_number_of_new_order_increases_in_work(self, login):
        order_list_page = OrderListPage(login)
        main_page = MainPage(login)
        number = main_page.make_an_order_and_get_number()
        main_page.go_to_orders_list()
        assert order_list_page.show_created_order_in_work(number)
