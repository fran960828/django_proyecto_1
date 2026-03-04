from django.db import models
from django.contrib.auth.models import User # Importamos el modelo de usuarios de Django

class News(models.Model):
    # Título de la noticia
    title = models.CharField(max_length=200, verbose_name="Título")
    
    # Contenido extenso de la noticia
    content = models.TextField(verbose_name="Contenido")
    
    # Fecha de creación: auto_now_add pone la fecha automáticamente al crear el registro
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    # Autor: Relacionamos la noticia con un usuario del sistema
    # on_delete=models.CASCADE significa que si se borra el usuario, se borran sus noticias
    author = models.CharField( verbose_name="Autor",max_length=50)
    
    # Casilla Booleana: True para mostrar, False para ocultar
    show_news = models.BooleanField(default=False, verbose_name="mostrar noticia")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-date_creation'] # Ordenar por defecto de las más nuevas a las más viejas

    def __str__(self):
        # Esto es lo que se verá en el panel de administrador
        return self.title
