from django.db import models
from areas.models import Area
from managers.models import Manager

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField(null=False)
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=200)

    areas = models.ForeignKey(Area, on_delete=models.CASCADE)
    managers = models.ManyToManyField(Manager, related_name='managers')

    def __str__(self):
        return self.nombre
