import pytest
from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in driver.page_source

def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.login("wronguser", "wrongpassword")

    error_text = login_page.get_error_message()
    assert "Your username is invalid!" in error_text