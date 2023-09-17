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

def test_google_search(driver):
    driver.get("https://google.com")
    googleSearchBox = driver.find_element(By.ID, "APjFqb")
    googleSearchBox.send_keys("Automation")
    time.sleep(1)
    googleSearchBox.send_keys(Keys.RETURN)
    time.sleep(1)
    print("Test completed.")

def test_naver_search(driver):
    driver.get("https://naver.com")
    driver.find_element(By.ID, "query").send_keys("Selenium")
    time.sleep(1)
    driver.find_element(By.ID, "query").send_keys(Keys.RETURN)
    time.sleep(1)
    print("naver test completed")
