import allure
from locators import locators


class registerPage:

    def __init__(self, driver):
        self.driver = driver
        self.account_button = locators.RegisterLocators.account_button
        self.reg_mail = locators.RegisterLocators.reg_mail
        self.password = locators.RegisterLocators.reg_password
        self.reg_button = locators.RegisterLocators.reg_button
        self.button_dsp = locators.RegisterLocators.logout_button_dsp

    def open_page(self):
        self.driver.get("http://skleptest.pl/")

    @allure.step("Creating a new account")
    def register(self, e_mail, password):
        self.driver.find_element(*self.account_button).click()
        self.driver.find_element(*self.reg_mail).send_keys(e_mail)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.reg_button).click()

    @allure.step("Check that the account has been created")
    def button_displayed(self):
        return self.driver.find_element(*self.button_dsp).is_enabled()








