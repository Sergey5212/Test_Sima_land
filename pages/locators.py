from selenium.webdriver.common.by import By


class FirstEntry():
    ALERT_BUTTON = (By.CSS_SELECTOR, "[data-testid='button']")
    BUTTON_CITY = (By.XPATH, "//div[@class='HFhf9']/div")


class AddingToLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='nav-item:cabinet']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-testid='register-link']")


class EnteringRegistrationData():
    NAME_REGISTRATION = (By.XPATH, "//div[@class='ojGKXh']//div[@class='Vhx81b']/div/input")
    CITY_REGISTRATION = (By.XPATH, "//div[@class='ojGKXh']//div[2]//div[@class='Vhx81b']/div/input")
    PHONE_REGISTRATION = (By.XPATH, "//div[@class='ojGKXh']//div[3]//div[@class='Vhx81b']/div/input")
    EMAIL_REGISTRATION = (By.XPATH, "//div[@class='ojGKXh']//div[4]//div[@class='Vhx81b']/div/input")
    PASSWORD_REGISTRATION = (By.XPATH, "//div[@class='ojGKXh']//div[5]//div[@class='Vhx81b']/div/input")
    REGISTER_BUTTON = (By.XPATH, "//div[@class='LxVmsx']/button")


class ButtonsOnTheMainPanel():
    CITY_MAIN_PANEL = (By.CLASS_NAME, "qjKhM")


class ProductSearch():
    PRODUCT_SEARCH_FIELD = (By.XPATH, "//div[@class='XVk3V']/input")
    BUTTON_SEARCH = (By.XPATH, "//div[@class=/fzq7C']//div/input")
    PRODUCT_IN_SEARCH = (By.CLASS_NAME, "jBE82l")
