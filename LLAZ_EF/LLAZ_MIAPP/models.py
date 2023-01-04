from django.db import models

# Create your models here.

class Docente(models.Model):
    codigo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    apellido_paterno=models.CharField(max_length=20)
    apellido_materno=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField()
    fecha_registro=models.DateField(auto_now_add=True)
    DNI=models.DateField(max_length=8)
    estado=models.CharField(max_length=20)