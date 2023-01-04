from django.db import models

# Create your models here.

class Docente(models.Model):
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    fecha_compra=models.DateField()
    fecha_registro=models.DateField(auto_now_add=True)
    estado=models.CharField(max_length=20)