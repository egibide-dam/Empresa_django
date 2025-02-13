from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre} ({self.telefono})"

class Habilidad (models.Model):
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.nombre}"

class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    def __str__(self):
        return f"{self.nombre} ({self.antiguedad})"



