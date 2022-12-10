import allure

from locators.locators import AddToCart

class AddToCartPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = AddToCart.add_to_cart_button
        self.my_cart_button = AddToCart.my_cart_button
        self.checkout_text = AddToCart.checkout_text

    def open_page(self):
        self.driver.get("http://skleptest.pl/")

    @allure.step("Adding  products to the cart ")
    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        self.driver.find_element(*self.my_cart_button).click()

    @allure.step("Checking if the products have been added to the cart")
    def checking_cart(self):
        return self.driver.find_element(*self.checkout_text).is_displayed()
