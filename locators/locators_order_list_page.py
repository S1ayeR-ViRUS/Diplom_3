from selenium.webdriver.common.by import By


class LocatorsOrderListPage:
    HEADER_ORDER_LIST = (By.XPATH, '//h1[text() = "Лента заказов"]')
    FIRST_ORDER_LIST = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][position() = (1)]')
    MODEL_ORDER_WINDOW = (By.XPATH, '//p[@class = "text text_type_main-medium mb-8"]')
    BLOCK_ORDERS_LIST = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li')
    ALL_ORDERS = (By.XPATH, './/p[@class="text text_type_digits-default"]')
    ALL_TIME_COUNT = (By.XPATH,
                      '/descendant::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"][position() = (1)]')
    TODAY_COUNT = (By.XPATH,
                   '/descendant::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"][position() = (2)]')
    ORDER_NUMBER_IN_WORK = (By.XPATH, '//ul[@class = "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li')
    BUTTON_CONSTRUCTOR = (By.XPATH, '//li/a[@href = "/"]')
