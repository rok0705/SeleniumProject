import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

options = Options()
options.add_experimental_option("detach", True)

chrome_driver = ChromeDriverManager().install()
print(chrome_driver)

# In Selenium3, (chrome_driver, options)
# In Selenium4, (service, options)
service = ChromeService(chrome_driver)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://naver.com")
