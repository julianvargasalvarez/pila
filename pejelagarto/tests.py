from django.test import TestCase
from models import Estudiante

class DatosBasicosProfesorRequeridosTest(TestCase):
    def test_longitud_nombre_mayor_a_cero(self):
        """
        Prueba que el nombre ingresado tenga una
        longitud mayor a cero.
        """
        profesor = Profesor()
        profesor.nombre = "Julian"
        profesor.save()

        p = Profesor.objects.all()[0]
        self.assertEqual(p.nombre, "Julian")

class DatosBasicosAcudienteRequeridosTest(TestCase):
    def test_longitud_nombre_mayor_a_cero(self):
        """
        Prueba que el nombre ingresado tenga una
        longitud mayor a cero.
        """
        acudiente = Acudiente()
        acudiente.edad = 0
        acudiente.nombre = "Julian"
        acudiente.save()

        a = Acudiente.objects.all()[0]
        self.assertEqual(a.nombre, "Julian")

class DatosBasicosEstudianteRequeridosTest(TestCase):
    def test_longitud_nombre_mayor_a_cero(self):
        """
        Prueba que el nombre ingresado tenga una
        longitud mayor a cero.
        """
        estudiante = Estudiante()
        estudiante.edad = 0
        estudiante.nombre = "Julian"
        estudiante.save()

        e = Estudiante.objects.all()[0]
        self.assertEqual(e.nombre, "Julian")

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
