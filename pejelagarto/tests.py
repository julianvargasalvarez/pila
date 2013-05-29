from django.test import TestCase
from models import Estudiante, Profesor, Acudiente, OrdenCompra, Producto


class DatosBasicosProfesorRequeridosTest(TestCase):
    def test_longitud_nombre_mayor_a_cero(self):
        """
        Prueba que el nombre ingresado tenga una
        longitud mayor a cero.
        """
        profesor = Profesor()
        profesor.nombre = "Julian"
        profesor.edad = 30
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
        acudiente.edad = 27
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

class DescuentoProgresivo(TestCase):
    def test_descuento_para_un_producto_es_cero(self):
        """
        Cuando el carro de compras tiene solo un producto
        el descuento aplicado es cero
        """
        carro = OrdenCompra()
        carro.save()

        carro.productos.add(Producto(precio=10.0))
        self.assertEqual(carro.total(), 10.0)

    def test_descuento_para_dos_productos_es_1_por_ciento(self):
        """
        Cuando el carro de compras tiene dos productos
        es descuento es del uno por ciento
        """
        carro = OrdenCompra()
        carro.save()

        carro.productos.add(Producto(precio=17.0))
        carro.productos.add(Producto(precio=13.0))
        self.assertEqual(carro.total(), 29.7)

    def test_descuento_para_tres_productos_es_1_por_ciento(self):
        """
        Cuando el carro de compras tiene tres productos
        es descuento es del uno por ciento
        """
        carro = OrdenCompra()
        carro.save()

        carro.productos.add(Producto(precio=17.0))
        carro.productos.add(Producto(precio=13.0))
        carro.productos.add(Producto(precio=5.0))

        self.assertEqual(carro.total(), 34.65)

    def test_descuento_para_cuatro_productos_es_2_por_ciento(self):
        """
        Cuando el carro de compras tiene cuatro productos
        es descuento es del dos por ciento
        """
        carro = OrdenCompra()
        carro.save()

        carro.productos.add(Producto(precio=17.0))
        carro.productos.add(Producto(precio=13.0))
        carro.productos.add(Producto(precio=5.0))
        carro.productos.add(Producto(precio=5.0))

        self.assertEqual(carro.total(), 39.2)

