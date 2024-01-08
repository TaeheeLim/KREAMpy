from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
from selenium.webdriver.common.keys import Keys
from module.Login import NaverLogin, EmailLogin, perform_login, User
from tkinter import messagebox

# Setup opitons
option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
# option.add_argument("start-maximized")
option.add_argument('disable-gpu')
#option.add_argument('headless')
option.add_argument('window-size=1920x1080')
option.add_experimental_option("detach", True)

def login(id, password, loginType):
    if not dataValiadation(id, password, loginType) :
        return

    print(id,password, loginType)

    # Selenium 4.0 - load webdriver
    try:
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s, options=option)
    except Exception as e:
        print(e)

    # Move to URL
    print('======================================================')
    print('==================매크로 시작 ..=======================')
    print('======================================================')

    browser.get('https://kream.co.kr/login')

    # 현재 URL 출력
    current_url = browser.current_url

    print(f"current URL: {current_url}")
    print('======================================================')

    user = User(id=id, password=password)

    if loginType == 1:
        login_method = EmailLogin()
    elif loginType == 2:
        login_method = NaverLogin()
    else:
        messagebox.showwarning('로그인 실패', '로그인 방식이 올바르지 않습니다.')
        return
    
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_login_naver')))
    perform_login(login_method, user, browser)

def dataValiadation(id, password, type):
    if type == 0:
        messagebox.showwarning('로그인 실패', '로그인 방식을 선택해주세요.')
        return False
    if id.strip() == '':
        messagebox.showwarning('로그인 실패', '아이디를 입력해주세요.')
        return False
    if password.strip() == '':
        messagebox.showwarning('로그인 실패', '비밀번호를 입력해주세요.')
        return False
    
    return True
