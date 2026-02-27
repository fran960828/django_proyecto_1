from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    precio_suscripcion = models.DecimalField(max_digits=6, decimal_places=2)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="series")
    categoria = models.CharField(max_length=50) # 'Sci-Fi', 'Drama', etc.

class Capitulo(models.Model):
    titulo = models.CharField(max_length=100)
    duracion_minutos = models.IntegerField()
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name="capitulos")
