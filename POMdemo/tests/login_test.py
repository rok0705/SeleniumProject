import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POMdemo.tests.pages.login_page import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("test", "test"),
    ("Steve", "Lee"),
    ("user2", "user2"),
])

def test_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_username(username)
    time.sleep(1)
    login_page.enter_password(password)
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)

    assert "Successful" in driver.page_source


