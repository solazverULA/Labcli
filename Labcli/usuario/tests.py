from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()



    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/usuario/registrar')

        #find the form element
        username = selenium.find_element_by_name('username')
        first_name = selenium.find_element_by_name('first_name')
        last_name = selenium.find_element_by_name('last_name')
        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_name('continue')

        #Fill the form with data
        username.send_keys('astridrm')
        first_name.send_keys('Astrid')
        last_name.send_keys('Rodriguez Molina')
        email.send_keys('astrid.rodriguez15@gmail.com')
        password1.send_keys('admin123')
        password2.send_keys('admin123')
        submit.send_keys(Keys.RETURN)



