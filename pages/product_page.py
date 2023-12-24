from .base_page import BasePage
from .locators import *


class ProductPage(BasePage):
    def find_a_product(self):
        self.browser.find_element(*ProductSearch.PRODUCT_SEARCH_FIELD).send_keys(
            'Кружка фарфоровая White Label, 350 мл, цвет белый')
        self.browser.find_element(*ProductSearch.BUTTON_SEARCH).click()

    def product_bar_and_basket(self):
        product_in_the_search_bar = self.browser.find_element(*ProductSearch.PRODUCT_SEARCH_FIELD).get_attribute('value')
        product_in_basket = self.browser.find_element(*ProductSearch.PRODUCT_IN_SEARCH).text
        assert product_in_the_search_bar.lower() == product_in_basket.lower()

    def should_be_page_product(self):
        self.find_a_product()
        self.product_bar_and_basket()
