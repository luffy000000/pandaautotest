from time import sleep
import unittest, sys
import ddt
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function, excelutil
from page_obj.loginpage import Login

excelpath = '/home/bruce/autotest/util/user.xls'
sheetname = 'Sheet1'
data = excelutil.ExcelUtil(excelpath, sheetname)
testdata = data.dict_data()

@ddt.ddt
class LoginTest(myunit.MyTest):

    @ddt.data(*testdata)
    def test_login(self, data):
        print ("当前测试数据%s" % data)
        Login(self.driver).user_login(username=data["username"], password=data["password"])
        po = Login(self.driver)
        result = po.is_login_success()
        try:
            self.assertTrue(result)
            function.insert_img(self.driver, 'success.png')
        except:
            function.insert_img(self.driver, 'error.png')
'''
    def test_login1(self):
        self.user_login_verify(username=self.data.dict_data()[0]['username'], password=self.data.dict_data()[0]['password'])
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), 'admin')
        function.insert_img(self.driver, 'success.png')

    def test_login2(self):
        self.user_login_verify(username=self.data.dict_data()[1]['username'], password=self.data.dict_data()[1]['password'])
        sleep(2)
        po = Login(self.driver)
        self.assertEqual(po.errot_hint(), u"用户名或密码错误")
        function.insert_img(self.driver, 'error.png')
'''

if __name__ == '__main__':
    unittest.main()
    