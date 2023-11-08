from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from selenium.webdriver.common.keys import Keys

# Setup opitons
option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
# option.add_argument("start-maximized")
option.add_argument('disable-gpu')
#option.add_argument('headless')
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

userId = 'lim3617'
userPassword = '#Mf4158kl0000'

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_login_naver')))
naverLogInButton = browser.find_element(By.CLASS_NAME, 'btn_login_naver')
naverLogInButton.click() # 버튼 클릭

print("로그인 창 열림")

WebDriverWait(browser, 10).until(lambda browser: len(browser.window_handles) > 1)

# 현재 윈도우 핸들 저장
main_window_handle = browser.current_window_handle
popup_window_handle = None

# 모든 윈도우 핸들을 검사하여 새 창으로 전환
for handle in browser.window_handles:
    print(handle)
    if handle != main_window_handle:
        popup_window_handle = handle
        break

# 새 창으로 컨텍스트 전환
browser.switch_to.window(popup_window_handle)
print(browser.title)

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'id')))
naverLogInId = browser.find_element(By.ID, 'id')
naverLogInId.send_keys(userId)

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'pw')))
naverLogInPw = browser.find_element(By.ID, 'pw')
naverLogInPw.send_keys(userPassword)

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'log.login')))
loginBtnWithNaver = browser.find_element(By.ID, 'log.login')
loginBtnWithNaver.click()

# 작업 완료 후 원래의 메인 윈도우로 다시 전환(필요한 경우)
#browser.switch_to.window(main_window_handle)