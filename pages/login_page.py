import allure
from locators import locators

class loginPage:

    def __init__(self, driver):
        self.driver = driver
        self.account_driver = locators.LoginLocators.account_button
        self.username_area = locators.LoginLocators.username_area
        self.password_area = locators.LoginLocators.password_area
        self.login_button = locators.LoginLocators.login_button
        self.error_msg = locators.LoginLocators.error_msg
        self.logout_area = locators.LoginLocators.logout_area


    def open_page(self):
        self.driver.get("http://skleptest.pl/")

    @allure.step("Login to the site using data username: {1} and password {2}")
    def log_in(self, username, password):
        self.driver.find_element(*self.account_driver).click()
        self.driver.find_element(*self.username_area).send_keys(username)
        self.driver.find_element(*self.password_area).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    @allure.step("Check if login was successful")
    def login_button_displayed(self):
        return self.driver.find_element(*self.logout_area).is_displayed()

    @allure.step("Entering incorrect data so that the login fails")
    def log_in_failed(self, username, password):
        self.driver.find_element(*self.account_driver).click()
        self.driver.find_element(*self.username_area).send_keys(username)
        self.driver.find_element(*self.password_area).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    @allure.step("Checking if login failed")
    def login_failed_displayed(self):
        return self.driver.find_element(*self.error_msg).text







