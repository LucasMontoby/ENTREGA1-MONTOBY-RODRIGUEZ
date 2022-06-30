from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    phone = models.IntegerField(verbose_name='Telefono')
    fecha_nacimiento = models.DateField(null=True)