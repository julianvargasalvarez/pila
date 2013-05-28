from django.db import models

class Estudiante(models.Model):
    edad = models.IntegerField()

    def es_mayor_de_edad(self):
        return self.edad > 17
