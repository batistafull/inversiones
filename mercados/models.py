from pyexpat import model
from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    apellido=models.CharField(max_length=50, verbose_name='Apellido')

    def __str__(self):
        return 'Mi nombre es %s %s' %(self.nombre, self.apellido)