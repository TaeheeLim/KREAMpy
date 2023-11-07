from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup opitons
option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
# option.add_argument("start-maximized")
option.add_argument('disable-gpu')
option.add_argument('headless')
option.add_argument('window-size=1920x1080')
option.add_experimental_option("detach", True)

# Selenium 4.0 - load webdriver
try:
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=option)
except Exception as e:
    print(e)

# Move to URL
browser.get('https://kream.co.kr/login')

# 페이지 제목 출력
page_title = browser.title
print(f"page title: {page_title}")

# 현재 URL 출력
current_url = browser.current_url
print(f"current URL: {current_url}")