from .base_page import BasePage
from .locators import *


class RegistrationPage(BasePage):
    def city_selection(self):
        self.browser.find_element(*FirstEntry.ALERT_BUTTON).click()

    def city_selection_2(self):
        self.browser.find_element(*FirstEntry.BUTTON_CITY).click()

    def press_button(self):
        self.browser.find_element(*AddingToLocators.LOGIN_BUTTON).click()

    def press_registration(self):
        self.browser.find_element(*AddingToLocators.CREATE_ACCOUNT_BUTTON).click()

    def entering_registration_data(self):
        self.browser.find_element(*EnteringRegistrationData.NAME_REGISTRATION).send_keys('Sergey98765432')
        self.browser.find_element(*EnteringRegistrationData.CITY_REGISTRATION).send_keys('Челябинск')
        self.browser.find_element(*EnteringRegistrationData.PHONE_REGISTRATION).send_keys(9779525188)
        self.browser.find_element(*EnteringRegistrationData.EMAIL_REGISTRATION).send_keys('sergey2000.02.29')
        self.browser.find_element(*EnteringRegistrationData.PASSWORD_REGISTRATION).send_keys('AsdfGhjkl12.,#')
        self.browser.find_element(*EnteringRegistrationData.REGISTER_BUTTON).click()

    def comparison_of_city_names(self):
        city_panel = self.browser.find_element(*ButtonsOnTheMainPanel.CITY_MAIN_PANEL).text
        city_registration = self.browser.find_element(*EnteringRegistrationData.CITY_REGISTRATION).text
        assert city_panel == city_registration
