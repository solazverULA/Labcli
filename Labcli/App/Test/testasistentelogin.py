# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestAsistent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_asistent(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(//a[contains(text(),'Login')])[2]").click()
       # time.sleep(5000)
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | name=username | ]]
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("asistente")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | name=password | ]]
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin123")
        driver.find_element_by_name("continue").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver Lista de Personas')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver Solicitudes')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver resultados')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Examenes')])[2]").click()
        driver.find_element_by_link_text("Editar").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver Lista de Paciente')])[2]").click()
        driver.find_element_by_link_text("Editar").click()
        driver.find_element_by_id("id_nombrepa").click()
        driver.find_element_by_id("id_nombrepa").clear()
        driver.find_element_by_id("id_nombrepa").send_keys("Diocelinaa")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()
