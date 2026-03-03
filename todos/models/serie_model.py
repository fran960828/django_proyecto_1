from django.db import models
from .director_model import Director

class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    precio_suscripcion = models.DecimalField(max_digits=6, decimal_places=2)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="series")
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo