from time import sleep
import unittest, sys
import pymysql
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function, database
from page_obj.accountpage import Account
from page_obj.loginpage import Login


class AccountTest(myunit.MyTest):

    
    def test_search(self):
        Login(self.driver).user_login()
        Account(self.driver).enter_account_manage()
        Account(self.driver).search_account('15927195782')
        self.assertEqual(Account(self.driver).search_success(), '15927195782')
        function.insert_img(self.driver, 'search_success.png')
    
    def test_a_send_gifts(self):
        self.test_search()
        Account(self.driver).send_gifts(166, 1)
        src = "select DISTINCT(gift_id) from app_uid_gift_four where uid in (select uid from app_user_attributes where phone='15927195782')"
        result = database.DataBase().execute_mysql(src)
        self.assertIn((166,), result)
        function.insert_img(self.driver, 'send_success.png')

    def test_recycle_gifts(self):
        self.test_search()
        sleep(2)
        Account(self.driver).recycle_gifts()
        src = "select DISTINCT(gift_id) from app_uid_gift_four where uid in (select uid from app_user_attributes where phone='15927195782')" 
        result = database.DataBase().execute_mysql(src)
        self.assertNotIn((166,), result)
        function.insert_img(self.driver, 'recycle_success.png')

if __name__ == '__main__':
    unittest.main()
        
        
        