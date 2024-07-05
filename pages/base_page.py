from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        self.driver.get(page_url)

    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(page_url))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_and_wait_element(self, locator):
        self.wait_for_load_element(locator)
        return self.find_element(locator)

    def find_elements(self, locator):
        self.wait_for_load_element(locator)
        return self.driver.find_elements(*locator)

    def click_element_with_wait(self, locator):
        element = self.find_and_wait_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_element(self, locator):
        self.find_and_wait_element(locator).click()

    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    def drag_and_drop_ingredient(self, locator1, locator2):
        ingredient = self.find_and_wait_element(locator1)
        target = self.find_and_wait_element(locator2)
        drag_and_drop(self.driver, ingredient, target)

    def wait_for_element_to_change_text(self, locator, text_to_be_changed):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(
            locator, text_to_be_changed))
        return self.driver.find_element(*locator)

    def check_element_is_invisible(self, locator):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.presence_of_element_located(locator))
        return True

    def format_locator(self, locator, num):
        method, locator_final = locator
        locator_final = locator_final.format(num)
        return method, locator_final
