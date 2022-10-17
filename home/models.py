from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    f_nac = models.DateField(null=True)
    f_creacion = models.DateField()

    def __str__(self):
        return f'Soy {self.nombre} {self.apellido}, de {self.edad} años'