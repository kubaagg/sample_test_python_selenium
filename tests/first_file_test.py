import pytest
import random
import pages.register_page
import pages.login_page
import pages.add_to_cart_page
import allure


@pytest.mark.usefixtures("setup")
class TestRegister:

    @allure.title("Register Test")
    @allure.description("Test creating a new account")
    def test_register(self):
        register = pages.register_page.registerPage(self.driver)
        register.open_page()
        register.register((str(random.randint(1, 10000)) + 'user@testuser.pl'), "usEr123@sas")

        assert register.button_displayed()

@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Login Test")
    def test_login(self):
        login = pages.login_page.loginPage(self.driver)
        login.open_page()
        login.log_in("testuser123@test.pl", "vAb!@#42563gbh&&*")

        assert login.login_button_displayed()

    @allure.title("Login failed test")
    def test_login_failed(self):
        login_failed = pages.login_page.loginPage(self.driver)
        login_failed.open_page()
        login_failed.log_in_failed("testuser@test.pl", "vAb!@#42563gbh&&*")

        assert "ERROR" or "Error" in login_failed.login_button_displayed()

@pytest.mark.usefixtures("setup")
class TestAddToCart:

    @allure.title("Adding products to the cart")
    def test_cart(self):
        cart = pages.add_to_cart_page.AddToCartPage(self.driver)
        cart.open_page()
        cart.add_to_cart()

        assert cart.checking_cart




