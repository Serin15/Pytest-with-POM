from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button.radius")
    error_message = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.error_message))
        return self.driver.find_element(*self.error_message).text
