from selenium.webdriver.common.by import By


class LocatorsMainPage:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text() = "Личный Кабинет"]')
    MAIN_PAGE = (By.CLASS_NAME, 'App_App__aOmNj')
    HEADER_MAIN_PAGE = (By.XPATH, '//h1[text() = "Соберите бургер"]')
    BUTTON_ORDER_LIST = (By.XPATH, '//p[text() = "Лента Заказов"]')
    BUTTON_CONSTRUCTOR = (By.XPATH, '//li/a[@href = "/"]')
    BUN_FIRST_IN_LIST = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    HEADER_MODAL_INGREDIENT = (By.XPATH, '//h2[text() = "Детали ингредиента"]')
    INGR_MODAL = (
        By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains(@class, "Modal_modal__container")]')
    BUTTON_CROSS_IN_MODAL_INGREDIENT = (
        By.XPATH, '//button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    BUN_IN_CONSTRUCTOR = (By.XPATH, '//section/ul/li[1]')
    BUTTON_CONFIRM_ORDER = (By.XPATH, '//button[text() = "Оформить заказ"]')
    BUTTON_CROSS_IN_MODAL = (By.XPATH,
                             '//button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    ORDER_NUMBER = (
        By.XPATH,
        '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    TEXT_IN_ORDER_MODAL = (By.XPATH, '//p[text() = "Ваш заказ начали готовить"]')
    COUNTER_INGREDIENT = (By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]')
