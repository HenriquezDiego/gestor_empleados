from django.db import models

class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class SubArea(models.Model):
    subarea_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    documento_identidad = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    subarea = models.ForeignKey(SubArea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
