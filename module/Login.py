from abc import ABC, abstractclassmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
from selenium.webdriver.common.keys import Keys

class User:
    def __init__(self, id, password):
        self.id = id
        self.password = password

class LoginInterface(ABC) :

    @abstractclassmethod
    def login(self, user, browser):
        pass

class NaverLogin(LoginInterface):

    def login(self, user : User, browser):
        naverLogInButton = browser.find_element(By.CLASS_NAME, 'btn_login_naver')
        naverLogInButton.click() # 버튼 클릭

        print('======================================================')
        print("로그인 창 열림")
        print('======================================================')

        WebDriverWait(browser, 10).until(lambda browser: len(browser.window_handles) > 1)

        # 현재 윈도우 핸들 저장
        main_window_handle = browser.current_window_handle
        popup_window_handle = None

        # 모든 윈도우 핸들을 검사하여 새 창으로 전환
        for handle in browser.window_handles:
            if handle != main_window_handle:
                popup_window_handle = handle
                break

        # 새 창으로 컨텍스트 전환
        browser.switch_to.window(popup_window_handle)

        print(f"팝업 브라우저 URL : {browser.current_url}")
        print('======================================================')

        pyperclip.copy(user.id)

        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'id')))
        naverLogInId = browser.find_element(By.ID, 'id')
        naverLogInId.click()
        naverLogInId.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        pyperclip.copy(user.password)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'pw')))
        naverLogInPw = browser.find_element(By.ID, 'pw')
        naverLogInPw.click()
        naverLogInPw.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'log.login')))
        loginBtnWithNaver = browser.find_element(By.ID, 'log.login')
        loginBtnWithNaver.click()

        print(browser.title)
        print(browser.current_url)

        # 작업 완료 후 원래의 메인 윈도우로 다시 전환(필요한 경우)
        browser.switch_to.window(main_window_handle)




class EmailLogin(LoginInterface):

    def login(self, user : User, browser):
        pyperclip.copy(user.id)

        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))
        naverLogInId = browser.find_element(By.XPATH, '//input[@type="email"]')
        naverLogInId.click()
        naverLogInId.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        pyperclip.copy(user.password)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
        naverLogInPw = browser.find_element(By.XPATH, '//input[@type="password"]')
        naverLogInPw.click()
        naverLogInPw.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.full.solid')))
        loginBtnWithNaver = browser.find_element(By.CSS_SELECTOR, 'a.btn.full.solid')
        loginBtnWithNaver.click()


def perform_login(login_method: LoginInterface, user : User, browser):
    login_method.login(user, browser)