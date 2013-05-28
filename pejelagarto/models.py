from django.db import models

class Estudiante(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=7)
    carne = models.CharField(max_length=7)

    def es_mayor_de_edad(self):
        return self.edad > 17

class Profesor(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=7)
    codigo = models.CharField(max_length=4)
    
    def es_mayor_de_edad(self):
        return self.edad > 17

     

class Acudiente(models.Model):
    edad = models.IntegerField()
    telefono = models.CharField(max_length=7)
    nombre = models.CharField(max_length=30)
    casado = models.BooleanField()

    def es_mayor_de_edad(self):
        return self.edad > 17

