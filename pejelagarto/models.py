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


