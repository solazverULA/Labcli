from django.test import TestCase
from django.contrib.auth.models import PermissionsMixin


from App.Paciente.models import Paciente

class PacienteModelTest(TestCase):

    def setUp(self):
        self.test_paciente = Paciente(nombrepa="Andres", apellidoma="Serrano", apellidopa="Rangel",
                                      sexo = "masculino", fecha_nac='2015-05-01', edad='3')
        self.test_paciente.save()

    def test_user_to_string_Paciente(self):
        self.assertEquals(str(self.test_paciente), "Andres Serrano")


    def tearDown(self):
        self.test_paciente.delete()


