from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from page_obj import basepage

class Account(basepage.BasePage):
    account_manage_loc = (By.XPATH, "//ul[@class='sidebar-menu']/li[6]/a/span[1]")
    account_handle_loc = (By.XPATH, "//ul[@class='sidebar-menu']/li[6]/ul/li/a")
    account_search_loc = (By.ID, 'query[name]')
    search_button_loc = (By.XPATH, "//form[@id='app-user-search-form']/div[2]/a")
 
    def enter_account_manage(self):
        self.find_element(*self.account_manage_loc).click()
        sleep(2)
        self.find_element(*self.account_handle_loc).click()
        sleep(2)

    def search_account(self, phone):
        self.find_element(*self.account_search_loc).clear()
        self.find_element(*self.account_search_loc).send_keys(phone)
        self.find_element(*self.search_button_loc).click()

    search_success_loc = (By.XPATH, "//table[@id='data_table']/tbody/tr/td[4]")

    def search_success(self):
        return self.find_element(*self.search_success_loc).text

    checkbox_loc = (By.XPATH, "//*[@id='data_table']/tbody/tr/td[1]/label/input")
    send_gifts_loc = (By.XPATH, "//*[@id='example1_wrapper']/div[2]/div/div/a")
    card_id_loc = (By.ID, 'card_id')
    card_num_loc = (By.ID, 'card_num')
    confirm_button_loc = (By.ID, "give-coupon-form-ok")
    account_detail_loc = (By.XPATH, "//table[@id='data_table']/tbody/tr/td[6]/a[1]")

    def send_gifts(self, card_id, card_num):
        self.find_element(*self.checkbox_loc).click()
        self.find_element(*self.send_gifts_loc).click()
        sleep(1)
        self.find_element(*self.card_id_loc).send_keys(card_id)
        self.find_element(*self.card_num_loc).send_keys(card_num)
        self.find_element(*self.confirm_button_loc).click()

    recycle_gifts_loc = (By.XPATH, "//table[@id='data_table_gift']/tbody/tr[5]/td[4]/a")

    def recycle_gifts(self):
        self.find_element(*self.account_detail_loc).click()
        sleep(2)
        self.find_element(*self.recycle_gifts_loc).click()


