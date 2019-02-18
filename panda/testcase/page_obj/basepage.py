class BasePage(object):
    '''
    页面基础类，用于所有页面的继承
    '''

    login_url = 'http://manage-sandbox.ximopanda.com/'

    def __init__(self, selenium_driver, base_url=login_url):
        self.driver = selenium_driver
        self.base_url = base_url

    def _open(self, url):
        self.driver.get(url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def switch_frame(self, loc):
        return self.driver.switch_to.frame(loc)

    def open(self):
        self._open(self.base_url)

    def script(self, src):
        return self.driver.execute_script(src)


