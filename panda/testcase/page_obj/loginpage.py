from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from page_obj import basepage

class Login(basepage.BasePage):

    # action
    login_username_loc = (By.ID, 'username')
    login_password_loc = (By.ID, 'password')
    login_button_loc = (By.ID, 'login_btn')
    confirm_loc = (By.XPATH, "//div[@class='icheckbox_square-blue']/ins")

    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    def confirm_login(self):
        self.find_element(*self.confirm_loc).click()

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username='admin', password='123456'):
        self.open()
        sleep(2)
        self.login_username(username)
        self.login_password(password)
        self.confirm_login()
        self.login_button()
        sleep(1)
    
    error_hint_loc = (By.XPATH, "//span[@class='text-danger']")
    user_login_success_loc = (By.XPATH, "//div[@class='pull-left info']/p")

    def is_login_success(self):
        try:
            text = self.find_element(*self.user_login_success_loc).text
            return True
        except:
            text = self.find_element(*self.error_hint_loc).text
            return False


'''
    # 用户名或密码错误
    def errot_hint(self):
        return self.find_element(*self.error_hint_loc).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
'''
