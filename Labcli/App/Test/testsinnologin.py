# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestSinLoguearse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sin_loguearse(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(//a[contains(text(),'Home')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Mi Resultado')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Crear Paciente')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver Lista de Paciente')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Crear Solicitud')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver Solicitudes')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Resultado de Examen')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Nuevo resultado')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver resultados')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Salir')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Registrarse')])[2]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Home')])[2]").click()

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
