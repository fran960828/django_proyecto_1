from django.db import models
from thumbnails.fields import ImageField 
from django_ckeditor_5.fields import CKEditor5Field

class Courses(models.Model):
    # Título de la noticia
    title = models.CharField(max_length=200, verbose_name="Nombre del curso")
    
    # Contenido extenso de la noticia
    content = CKEditor5Field('Content', config_name='default')
    
    # Fecha de creación: auto_now_add pone la fecha automáticamente al crear el registro
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    # Casilla Booleana: True para mostrar, False para ocultar
    show_course = models.BooleanField(default=False, verbose_name="mostrar curso")

    topics = models.FileField(upload_to='tempario/pdf/', null=True, blank=True)

    main_image=ImageField(upload_to='image/',null=True , blank=True)

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['-date_creation'] # Ordenar por defecto de las más nuevas a las más viejas

    def __str__(self):
        # Esto es lo que se verá en el panel de administrador
        return self.title

# Create your models here.
