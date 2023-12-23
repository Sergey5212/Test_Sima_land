import pytest
from .pages.registration_page import RegistrationPage

link_registration = "https://www.sima-land.ru/"


@pytest.mark.first_registration
class TestNewRegistrationUser:
    def test_login_and_data_entry(self, browser):
        pages = RegistrationPage(browser, link_registration)
        pages.open()
        pages.city_selection()
        pages.city_selection_2()
        pages.press_button()
        pages.press_registration()
        pages.entering_registration_data()
