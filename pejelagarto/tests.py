from django.test import TestCase
from models import Estudiante

class MayorEdadTest(TestCase):
    def test_es_mayor_de_edad_con_18(self):
        """
        Prueba que el estudiante es mayor de edad
        cuando la edad es 18.
        """
        estudiante = Estudiante()
        estudiante.edad = 18
        self.assertEqual(estudiante.es_mayor_de_edad(), True)

    def test_es_mayor_de_edad_con_mas_de_18(self):
        """
        Prueba que el estudiante es mayor de edad
        cuando la edad es > 18.
        """
        estudiante = Estudiante()
        estudiante.edad = 19
        self.assertEqual(estudiante.es_mayor_de_edad(), True)

    def test_no_es_mayor_de_edad_con_menos_de_18(self):
        """
        Prueba que el estudiante no es mayor de edad
        cuando la edad es < 18.
        """
        estudiante = Estudiante()
        estudiante.edad = 17
        self.assertEqual(estudiante.es_mayor_de_edad(), False)
