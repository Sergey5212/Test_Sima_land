import pytest
from pages.product_page import ProductPage

link_registration = "https://www.sima-land.ru/"


@pytest.mark.product_check
class TestProductAvailability():
    def test_city_match(self, browser):
        pages = ProductPage(browser, link_registration)
        pages.open()
        pages.should_be_page_product()
