from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/usuario/registrar')

        #find the form element
        username = selenium.find_element_by_id("username")
        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')

        submit = selenium.find_element_by_name('continue')

        #Fill the form with data
        username.send_keys('astridrm')
        email.send_keys('astrid.rodriguez15@gmail.com')
        password1.send_keys('123456')
        password2.send_keys('123456')

