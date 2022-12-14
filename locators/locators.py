from selenium.webdriver.common.by import By



class RegisterLocators:

    account_button = (By.XPATH, "//li[@class='top-account']//a")
    reg_mail = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    reg_button = (By.NAME, "register")
    logout_button_dsp = (By.XPATH, "//a[.='Log out']")
    logout_butt = (By.NAME, "register") #send keys click enter
class LoginLocators:

    account_button = (By.XPATH, "//li[@class='top-account']//a")
    username_area = (By.ID, "username")
    password_area = (By.ID, "password")
    login_button = (By.NAME, "login")
    error_msg = (By.XPATH, "//ul[@class='woocommerce-error']//strong")
    logout_area = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']//a")

class AddToCart:


    add_to_cart_button = (By.XPATH, "//a[@rel]")
    my_cart_button = (By.XPATH, "//li[@class='top-cart']//a")
    checkout_text = (By.LINK_TEXT, "Proceed to checkout")




