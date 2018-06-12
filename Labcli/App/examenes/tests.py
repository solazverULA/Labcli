from django.test import TestCase
from django.contrib.auth.models import PermissionsMixin
import time
# Create your tests here.

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    #Para poder crear un nuevo examen debe estar logeado como asistente o bioanalista
    def test_iniciarsesion(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/examenes/Crear')

        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_name('continue')

        #Fill the form with data
        username.send_keys('asistente')
        password.send_keys('admin123')
        submit.send_keys(Keys.RETURN)

