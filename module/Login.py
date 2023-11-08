from abc import ABC, abstractclassmethod
from ..object.User import User

class LoginInterface(ABC) :


    @abstractclassmethod
    def login(self, user, browser):
        pass

class NaverLogin(LoginInterface):

    def login(self, user : User, browser):
        print('네이버 로그인 중 . . .')
        print(f"현재 사용자 : {user}")
        print(f"현재 브라우저 : {browser}")    

class EmailLogin(LoginInterface):

    def login(self, user : User, browser):
        print('이메일 로그인 중 . . .')
        print(f"현재 사용자 : {user}")
        print(f"현재 브라우저 : {browser}")

def perform_login(login_method: LoginInterface, user : User, browser):
    login_method.login(user, browser)

# 각 로그인 메커니즘에 대한 인스턴스 생성
#password_login = NaverLogin()
#token_login = EmailLogin()

# 로그인 실행
#perform_login(password_login)
#perform_login(token_login)