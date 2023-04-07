from django.db import models

class Familiar(models.Model):

    nombre = models.TextField(max_length=40)
    edad = models.IntegerField()
    fecha_nac=models.DateField(default="1989-11-28")
    parentezco= models.TextField(max_length=10)

    def __str__(self):
        return f"Nombre: {self.nombre} - Parentezco= {self.parentezco} - Nac: {self.fecha_nac}"


# Create your models here.
