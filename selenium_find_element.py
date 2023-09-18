import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#<input id="query" name="query" type="search" title="검색어를 입력해 주세요."
#placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
driver.get("https://www.naver.com")
driver.find_element(By.CLASS_NAME, "search_input").send_keys("블랙핑크")
time.sleep(1)

driver.find_element(By.ID, "query").send_keys("뉴진스")
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='query']").send_keys("트와이스")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "[placeholder='검색어를 입력해 주세요.']").send_keys("에스파")
time.sleep(1)

#driver.find_element(By.LINK_TEXT, "쇼핑").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "동산").click()
time.sleep(1)

serviceList = driver.find_elements(By.CSS_SELECTOR, "[class='link_service']")
for service in serviceList:
    print(service.get_attribute("outerHTML"))
    print()

time.sleep(10)
