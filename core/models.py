

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactMessage(models.Model):
    """
    Modelo para almacenar los mensajes enviados a través del formulario de contacto.
    """
    name = models.CharField(
        max_length=100, 
        verbose_name=_("Nombre")
    )
    email = models.EmailField(
        verbose_name=_("Correo electrónico")
    )
    message = models.TextField(
        verbose_name=_("Comentario")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_("Enviado el")
    )
    is_read = models.BooleanField(
        default=False, 
        verbose_name=_("¿Leído?")
    )

    class Meta:
        verbose_name = _("Mensaje de contacto")
        verbose_name_plural = _("Mensajes de contacto")
        ordering = ['-created_at']  # Los más recientes primero

    def __str__(self):
        return f"{self.name} - {self.email} ({self.created_at.strftime('%d/%m/%Y')})"