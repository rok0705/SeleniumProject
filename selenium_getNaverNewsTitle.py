import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.naver.com")
time.sleep(1)

#<input id="query" name="query" type="search" title="검색어를 입력해 주세요."
#placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
searchBox = driver.find_element(By.CSS_SELECTOR, "[placeholder='검색어를 입력해 주세요.']")
searchBox.send_keys("무빙 드라마")
time.sleep(1)

searchReturn = driver.find_element(By.CSS_SELECTOR, "[class='btn_search']")
searchReturn.click()
time.sleep(1)

#<i class="spnew2 ico_nav_view"></i>
viewButton = driver.find_element(By.CSS_SELECTOR, "[class='spnew2 ico_nav_view']")
viewButton.click()
time.sleep(1)

for i in range(4):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

#<a href="https://blog.naver.com/rhkdgus772/223162313386" class="api_txt_lines total_tit _cross_trigger"
#data-cr-gdid="90000003_0000000000000033F582AAAA" target="_blank" onclick="return goOtherCR(this, 'a=rvw*b.link&amp;r=4&amp;
# i=90000003_0000000000000033F582AAAA&amp;u='+urlencode(this.href))"><mark>파이썬</mark> 학원 개발자 되기 위한 준비과정</a>
titles = driver.find_elements(By.CSS_SELECTOR, "[class='api_txt_lines total_tit _cross_trigger']")
for e, title in enumerate(titles, 1):
    print(f"{e} : {title.text}")