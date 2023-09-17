import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

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
    driver.get("https://trytestingthis.netlify.app/index.html")
    driver.find_element(By.ID, "uname").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "pwd").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(3)

    assert "Successful" in driver.page_source


