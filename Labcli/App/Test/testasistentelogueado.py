# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestAsistentelogueado(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_asistentelogueado(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(//a[contains(text(),'Registrar Persona')])[2]").click()
        driver.find_element_by_id("id_cedula").click()
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("V202372661")
        driver.find_element_by_id("id_nombrepa").click()
        driver.find_element_by_id("id_nombrepa").clear()
        driver.find_element_by_id("id_nombrepa").send_keys("astrid")
        driver.find_element_by_id("id_apellidopa").click()
        driver.find_element_by_id("id_apellidopa").clear()
        driver.find_element_by_id("id_apellidopa").send_keys("rodriguez")
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div").click()
        driver.find_element_by_id("id_apellidoma").click()
        driver.find_element_by_id("id_apellidoma").clear()
        driver.find_element_by_id("id_apellidoma").send_keys("molina")
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div").click()
        driver.find_element_by_id("id_sexo").click()
        Select(driver.find_element_by_id("id_sexo")).select_by_visible_text("Femenino")
        driver.find_element_by_xpath("//option[@value='F']").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div/div/form/p[6]/span").click()
        driver.find_element_by_id("id_fecha_nac").click()
        driver.find_element_by_id("id_fecha_nac").clear()
        driver.find_element_by_id("id_fecha_nac").send_keys("1995-08-01")
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div").click()
        driver.find_element_by_id("id_telefono").click()
        driver.find_element_by_id("id_telefono").clear()
        driver.find_element_by_id("id_telefono").send_keys("04247370988")
        driver.find_element_by_id("id_domicilio").click()
        driver.find_element_by_id("id_domicilio").clear()
        driver.find_element_by_id("id_domicilio").send_keys("El vigia, la palmita.")
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div").click()
        driver.find_element_by_id("id_user").click()
        Select(driver.find_element_by_id("id_user")).select_by_visible_text("astrid_lisa")
        driver.find_element_by_xpath("//option[@value='11']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_cedula").click()
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("V2023726613")
        driver.find_element_by_id("id_user").click()
        Select(driver.find_element_by_id("id_user")).select_by_visible_text("milagrorojas")
        driver.find_element_by_xpath("//option[@value='3']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_cedula").click()
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("V2023726614")
        driver.find_element_by_id("id_apellidoma").click()
        driver.find_element_by_id("id_apellidoma").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_apellidoma | ]]
        driver.find_element_by_id("id_apellidoma").clear()
        driver.find_element_by_id("id_apellidoma").send_keys(u"briceño")
        driver.find_element_by_id("id_user").click()
        Select(driver.find_element_by_id("id_user")).select_by_visible_text("asistente")
        driver.find_element_by_xpath("//option[@value='5']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_cedula").click()
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("V023726614")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_user").click()
        Select(driver.find_element_by_id("id_user")).select_by_visible_text("maximourdaneta")
        driver.find_element_by_xpath("//option[@value='7']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_cedula").click()
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("V023726615")
        driver.find_element_by_id("page").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("page").click()
        driver.find_element_by_id("id_user").click()
        Select(driver.find_element_by_id("id_user")).select_by_visible_text("diocelinacontreras")
        driver.find_element_by_xpath("//option[@value='10']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_cedula").click()
        driver.find_element_by_id("id_cedula").click()
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("V023726618")
        driver.find_element_by_id("page").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div/div/form/p[9]").click()
        driver.find_element_by_id("id_user").click()
        Select(driver.find_element_by_id("id_user")).select_by_visible_text("astrid_lisarm")
        driver.find_element_by_xpath("//option[@value='12']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Crear Solicitud')])[2]").click()
        driver.find_element_by_id("id_fecha_sol").click()
        driver.find_element_by_id("id_fecha_sol").clear()
        driver.find_element_by_id("id_fecha_sol").send_keys("2018-06-26")
        driver.find_element_by_id("id_paciente").click()
        Select(driver.find_element_by_id("id_paciente")).select_by_visible_text("astrid rodriguez astrid_lisarm")
        driver.find_element_by_xpath("//option[@value='9']").click()
        driver.find_element_by_id("id_examenes_0").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]").click()
        driver.find_element_by_id("id_pagado").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Nuevo resultado')])[2]").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div/div").click()
        driver.find_element_by_id("id_paciente").click()
        Select(driver.find_element_by_id("id_paciente")).select_by_visible_text("astrid rodriguez astrid_lisarm")
        driver.find_element_by_xpath("//option[@value='9']").click()
        driver.find_element_by_id("id_solicitud").click()
        Select(driver.find_element_by_id("id_solicitud")).select_by_visible_text(
            "Id Solicitud: 9 Datos:astrid rodriguez Pago: True")
        driver.find_element_by_xpath("(//option[@value='9'])[2]").click()
        driver.find_element_by_id("id_detalle_examen_set-0-examenes").click()
        Select(driver.find_element_by_id("id_detalle_examen_set-0-examenes")).select_by_visible_text(
            "nombre: Hemoglobina Rango: 12-15")
        driver.find_element_by_xpath("(//option[@value='1'])[3]").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div/div/div/form/table/tbody/tr/td[2]").click()
        driver.find_element_by_id("id_detalle_examen_set-0-valores").click()
        driver.find_element_by_id("id_detalle_examen_set-0-valores").clear()
        driver.find_element_by_id("id_detalle_examen_set-0-valores").send_keys("13")
        driver.find_element_by_xpath("//input[@value='Save']").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Ver resultados')])[2]").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div/div/section/table/tbody/tr[11]/td[6]").click()
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div/div/div/section/table/tbody/tr[11]/td[6]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //div[@id='page']/div[2]/div/div/div/section/table/tbody/tr[11]/td[6] | ]]
        driver.find_element_by_xpath("//div[@id='page']/div[2]/div").click()

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
