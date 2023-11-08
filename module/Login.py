from abc import ABC, abstractclassmethod

class LoginInterface(ABC) :

    @abstractclassmethod
    def login(self):
        pass

class NaverLogin(LoginInterface):

    def login(self, user):
        print("네이버로 로그인을 시도합니다.")
    

class EmailLogin(LoginInterface):

    def login(self, user):
        print("이메일로 로그인을 시도합니다.")

def perform_login(login_method: LoginInterface, user):
    login_method.login(user)

# 각 로그인 메커니즘에 대한 인스턴스 생성
#password_login = NaverLogin()
#token_login = EmailLogin()

# 로그인 실행
#perform_login(password_login)
#perform_login(token_login)