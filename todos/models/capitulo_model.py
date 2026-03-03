from django.db import models
from .serie_model import Serie

class Capitulo(models.Model):
    titulo = models.CharField(max_length=100)
    duracion_minutos = models.IntegerField()
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name="capitulos")
    def __str__(self):
        return self.titulo