import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

options = Options()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/60.0.5195.102 Safari/537.36"

options.add_argument(f"user-agent={user_agent}")
# 프로그램 끝나고 창살릴때
options.add_experimental_option("detach", True)
# 풀스크린
# options.add_argument("--start-maximized")
# F11
# options.add_argument("--start-fullscreen")
# 커스텀사이즈
# options.add_argument("window-size=500,500")
# 백그라운드로 실행
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# 사운드 off
#options.add_argument("--mute-audio")
# 시크릿창
#options.add_argument("incognito")

#options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chrome is being controlled by automation software 메세지 없애기.
#options.add_experimental_option("excludeSwitches", ["enable-automation"])

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://naver.com")

#(driver.page_source[:1000])
