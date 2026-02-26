from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField('Nombre',max_length=30)
    last_name=models.CharField('Apellido',max_length=30)
    age=models.IntegerField('Edad',default=18,help_text='Introduce tu edad en formato numerico')
    dni=models.CharField('DNI',max_length=9,unique=True)
