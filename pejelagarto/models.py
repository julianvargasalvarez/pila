from django.db import models

class Persona(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=7)

    def es_mayor_de_edad(self):
        return self.edad > 17
    
    class Meta:
        abstract = True


class Estudiante(Persona):
    carne = models.CharField(max_length=7)


class Profesor(Persona):
    codigo = models.CharField(max_length=4)

class Acudiente(Persona):
    casado = models.BooleanField()


class OrdenCompra(models.Model):

    productos = models.ManyToManyField('Producto')

    def sub_total(self):
        total = self.productos.all().aggregate(models.Sum('precio'))
        return total['precio__sum']
    def aplicar_descuentos(self):
        sub_total = self.sub_total()
        cantidad = self.productos.count()
        if cantidad == 2 or cantidad==3:
            sub_total = sub_total - (sub_total*0.01)
        elif cantidad == 4:
            sub_total = sub_total - (sub_total*0.02)
        return sub_total

    def total(self):
        return self.aplicar_descuentos()

class ProductoManager(models.Manager):
    def cantidad_productos_vendidos(self):
        return self.all().count()

class Producto(models.Model):
    precio = models.FloatField()
    objects = ProductoManager()
