from django.db import models

class Estudiante(models.Model):
    edad = models.IntegerField()
    nombre = models.CharField(max_length=30)

    def es_mayor_de_edad(self):
        return self.edad > 17
